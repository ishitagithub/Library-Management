#ishita
import mysql.connector
mydb=mysql.connector.connect(user='root',
                                 host='localhost',
                                 password='Ishita.mysql')
mycur=mydb.cursor(buffered=True)


#made by ishita
def issue_date():
    import datetime
    d=datetime.datetime.now
    return str(d().date())

mycur.execute("use library")

def issuebook():
        ad=int(input("enter your admnno"))
        mycur.execute("select * from students")
        count=0
        c=0
        for i in mycur:
            
            # for checking whether name of student is there
            if i[0]==ad:
                print(i[1])
                bk=input("Enter book u want to issue")
                book=bk.lower()
                mycur.execute("select * from bookdetails")
                count+=1

                
                for i in mycur:
                    # for checking whether book is there
                    if i[1]==book and i[3]=='yes':
                        d=issue_date()
                        bookid=i[0]

                        mycur.execute('select max(issue_id) from book_records')
                        for i in mycur:
                            issueid=i[0]+1
                        

                        #using book_records table
                        mycur.execute("select * from book_records")
                        v=("insert into book_records(issue_id,bookid,issue_date,admn_no) values(%s,%s, %s,%s)")
                        issue=(issueid,bookid,d,ad)
                        mycur.execute(v,issue)
                        c+=1
                        print("You have successfully issued the book with issue id",issueid)
                        print("You have to return this book in one week, otherwise,penalty 10 ruppees per day will be charged")
                        
                        # for changing book details
                        print("BOOKID of issued book is",bookid )
                        
                        up=("update bookdetails set avail_status='no' where Bookid =%s")
                        t=(bookid,)
                        mycur.execute(up,t)
                        mydb.commit()
                        break


                    
        if count==0:
            print("FIRST ASK YOUR TEACHER TO ADD NAME IN STUDENT RECORDS")
        if c==0 and count!=0:
            print("SORRY,THIS BOOK IS NOT IN LIBRARY")#needed to add return date
       #ishita     
