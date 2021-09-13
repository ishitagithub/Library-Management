#ishita
import mysql.connector
mydb=mysql.connector.connect(user='root',
                                 host='localhost',
                                 password='Ishita.mysql')
mycur=mydb.cursor(buffered=True)
mycur.execute("use library")
def searchstud():
        mycur.execute("select * from students")
        bk=int(input("Enter admnno u want to search about"))
        count=0
        for i in mycur:
            if i[0]==bk:   #books details are stored as tuple
                print("Student details are")
                print("ADMN NO:",i[0])
                print("NAME:",i[1])
                print("PENALTY:",i[2])
                
                count+=1
        if count==0:
                print("SORRY, the student name is not in the library")




#ishita

def penstud():
        mycur.execute("select * from students")
        count=0
        mycur.execute("select * from students where penalty is not null")
        for i in mycur:
                if i[2]!=0:
                
                        print("Student details are")
                        print("ADMN NO:",i[0])
                        print("NAME:",i[1])
                        print("PENALTY:",i[2])

                        count+=1
                
        if count==0:
                print("NO PENALTY OF ANY STUDENT")
                #ishita
