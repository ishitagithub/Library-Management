#ishita
import mysql.connector
mydb=mysql.connector.connect(user='root',
                                 host='localhost',
                                 password='Ishita.mysql')
mycur=mydb.cursor(buffered=True)


mycur.execute("use library")
def issuereport():
    ad=int(input("Enter your admn no"))
   
    mycur.execute("select * from book_records")
    c=0
    for i in mycur:
        if i[3]==ad:
            print("issue id",i[0])
            print("bookid",i[1])
            print("issue date",i[2])
            print("return date",i[4])
            print("Penalty",i[5])
            print("===============================================")
            c+=1
    if c==0:
        print("You have not issued book")
            





#ishita

def penreport():
    ad=int(input("Enter your admn no"))
    mycur.execute("select * from students")
    mycur.execute("select * from students where penalty is not null")
    c=0
    for i in mycur:
        if i[2]!=0 and i[0]==ad:
            print("penalty",i[2])
            c+=1
            
    if c==0:
        print("No Penalty")
   
    




def stud():
        mycur.execute("select * from students")
        bk=int(input("Enter   your admnno "))
        count=0
        for i in mycur:
            if i[0]==bk:   #books details are stored as tuple
                print("Student details are")
                print("ADMN NO:",i[0])
                print("NAME:",i[1])
                print("PENALTY:",i[2])
                count+=1


        if count==0:
            print("Your account is not there")
                
 #ishita               
