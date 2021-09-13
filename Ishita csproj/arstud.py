#ishita
import mysql.connector
mydb=mysql.connector.connect(user='root',
                                 host='localhost',
                                 password='Ishita.mysql')
mycur=mydb.cursor(buffered=True)

mycur.execute("use library")

def addstudent():
        mycur.execute("use library")
        admn=int(input("Enter admission no."))
    
        mycur.execute("select * from students")
        count=0
        for i in mycur:
            if i[0]==admn:
                print("Account already exist")
                count+=1
        if count==0:
            v="insert into students(admn_no,name) values(%s, %s)"
            b=str(input("Enter name:"))
            name=b.lower()
            book=(admn,name)
            mycur.execute(v,book)
            mydb.commit()
            print("Your name has been successfully added")
            #made by ishita
def removestud():
        ad=input("Enter admn no. u want to delete")
        mycur.execute("select * from students")
        count=0
        for i in mycur:
                
            if i[0]==int(ad):
                    
                c="delete from book_records where admn_no="+ad
                b="delete from students where admn_no="+ad
                mycur.execute(c)
                mycur.execute(b)
                mydb.commit()
                print("The student record has been successfully been deleted")
                count+=1
                
        if count==0:
            print("Sorry this student record is not in the library")
#ishita
