school_name ='KENDRIYA VIDYALAYA'
school_address ='Sector 24 noida'
school_email = 'noida_kv@rediffmail.com'
school_phone ='0120-2411484'
import mysql.connector
mycon=mysql.connector.connect(
  user='root',
 password='password', #enter your mysql password here
  database='school')  #enter the name of database here
cur=mycon.cursor()

def addstudent():
    print('Add New Student Screen')
    print('-'*120)
    nm=input("Enter Student's name : ")
    fn=input("Enter Father's name : ")
    cls=input("Enter Class :")
    rlln=input("Enter Roll no :")
    sc=input("Enter Section :")
    admno = input('Enter Admission NO :')
    s="INSERT INTO student(admn,name, fathers_name,class,section,roll_no)VALUES (%s,%s,%s,%s,%s,%s)"
    info=(admno,nm,fn,cls,sc,rlln)
    cur.execute(s,info)
    mycon.commit()
    print('\n\n\n New Student added successfully.....')
    wait=input('\n\n\nPress any key to continue...')

                                                                                                                                        


def addmarks():

print('Add New marks Screen')
    print('-'*120)
    admno = input('Enter admission NO :')
    nm=input("Enter student's name : ")
    cls=input("enter student's class : ")
    sessionn = input('Enter session  : ')
    phy = input('Enter marks in Physics : ')
    chem = input('Enter marks in Chemistry : ')
    maths = input('Enter marks in maths : ')
    eng = input('Enter marks in English : ')
    css = input('Enter marks in Computer science : ')
    d="INSERT INTO marks(admn,name,class,session,physics,chemistry,math,english,cs) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    stu=(admno,nm,cls,sessionn,phy,chem,maths,eng,css)
    cur.execute(d,stu)
mycon.commit()







def modify_student():
    print("______________MODIFY STUDENT SCREEN_________________")
    admno = input('Enter admission No :')
    print('\n1.   Name  ')
    print('\n2.   Father Name  ')
    print('\n3.   Class  ')
    print('\n4.   Section  ')
    print('\n\n')
    choice = int(input('Enter your choice :'))
    field=''
    if choice ==1:
       field ='name' 
    if choice == 2:
       field = 'fathers_name'
    if choice == 3:
       field = 'class'
    if choice == 4:
       field = 'section'
    value =input('Enter new value :')
    ad='update student set '+field+' ="'+value +'" where admn ='+admno+';'
    cur.execute(ad)
    mycon.commit()
    print('\n\n\n Student Record Updated.....')
    wait = input('\n\n\nPress any key to continue......')


def modify_marks():
    print('_______________Modify Marks - Screen_________________')
    print('-'*120)
    admno = input('Enter admission No :')
    sessionn = input('Enter Session  :')
    print('\n1.   Physics  ')
    print('\n2.   Chemistry  ')
    print('\n3.   Mathematics  ')
    print('\n4.   English  ')
    print('\n5.   Computer  ')
    print('\n\n')
    choice = int(input('Enter your choice :'))
    field = ''
    if choice == 1:
       field = 'physics'
    if choice == 2:
       field = 'chemistry'
    if choice == 3:
       field = 'math'
    if choice == 4:
       field = 'english'
    if choice == 5:
       field = 'cs'

    value = input('Enter new value :')
    sql = 'update marks set '+field+' ='+value + ' where admn ='+admno+'  AND session="'+sessionn+'";'
    cur.execute(sql)
    mycon.commit()
    print('\n\n\n Marks Updated.....')
    wait = input('\n\n\nPress any key to continue......')


def search_student():
  print("______________________SEARCH STUDENT SCREEN___________________________")
  admno = input('Enter admission No :')
  db='select * from student where admn='+admno+' ;'
  cur.execute(db)
  records=cur.fetchall()
  print('Search Result for Admission No :'+admno +'')
  print('-'*120)
  for record in records:
      print(record)
  wait = input('\n\n\n Press any key to continue.....')



def search_marks():
    admno = input('Enter admission No :')
    sessionn = input('Enter Session  :')
    sql ='select * from marks where admn = '+admno + ' and session ="'+ sessionn+'";'
    cur.execute(sql)
    records = cur.fetchall()
    print('Search Result for Admission No :'+admno +',  Session : '+sessionn+'')
    print('-'*120)
    for record in records:
      print(record)
wait = input('\n\n\n Press any key to continue.....')



def search_menu():
    while True:
      print(' S E A R C H    M E N U')
      print('-'*120)
      print("\n1.  Admission No")
      print('\n2.  Name / Father Name')
      print('\n3.  Student Term Marks')
      print('\n4.  back to main')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))
      field=''
      if choice == 1:
        field='admn'
        search_student()
      if choice == 2:
        field='name'
        search_student()
      if choice == 3:
        search_marks()
      if choice == 4:
        break

from prettytable import PrettyTable
def report_whole_class():
    cls = input('Enter Class :')
    sc =input ('Enter section :')
    sessionn = input('Enter Session  :')
    cur.execute( "select * from marks  where class="+cls+';')
    data=cur.fetchall()
    print(data)
    print(school_name)
    print(school_address)
    print('Phone :',school_phone ,' Email :', school_email)
    print('-'*120)
    print('Class Wise Report Card:',cls,'-',sc, 'Session : ',sessionn )
    print('-'*120)
    mytable = PrettyTable(["admno",  "Name", "Phy", "Chem", "Math","Eng","cs"])
    for  admn,name,cls,section,physics,chemistry,math,english,cs in data:
      mytable.add_row([ admn,name, physics, chemistry, math, english, cs])
    print(mytable)
    wait = input('\n\n\n Press any key to continue.....')

def main_menu():
    while True:
      print(' R E P O R T   C A R D   M E N U  ')
      print("\n1.  Add Student")
      print('\n2.  Modify Student Record')
      print('\n3.  Add marks')
      print('\n4.  Modify Marks')
      print('\n5.  Search Menu')
      print('\n6.  whole class report card')
      print('\n7.  Close application')
      print("\n\n")
      choice = int(input('Enter your choice ...: '))
      if choice == 1:
        addstudent()
      if choice == 2:
        modify_student()
      if choice == 3:
        addmarks()
      if choice == 4:
        modify_marks()
      if choice == 5:
        search_menu()
      if choice == 6:
        report_whole_class()
      if choice == 7:
        break
main_menu()
