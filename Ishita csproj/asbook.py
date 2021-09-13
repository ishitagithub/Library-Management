#ishita
import mysql.connector
mydb=mysql.connector.connect(user='root',
                                 host='localhost',
                                 password='Ishita.mysql')
mycur=mydb.cursor(buffered=True)
mycur.execute("use library")
def addbook():
            v="insert into bookdetails values(%s, %s, %s,%s)"
            mycur.execute('select max(bookid) from bookdetails')
            for i in mycur:
                bookid=i[0]+1
    
            tit=str(input("enter book title"))
            title=tit.lower()
            auth=str(input("enter book author"))
            author=auth.lower()

            book=(bookid,title,author,'yes')
            mycur.execute(v,book)
            mydb.commit()
       
            print("This book has been successfully added in the library with bookid",bookid)


#made by ishita
            
def searchbook():
        mycur.execute("select * from bookdetails")
        bk=str(input("Enter book u want to search about"))
        book=bk.lower()
        count=0
        for i in mycur:
            if i[1]==book:   #books details are stored as tuple
                print("Book details are")
                print("BOOK ID:",i[0])
                print("BOOK NAME:",i[1])
                print("BOOK AUTHOR:",i[2])
                print("AVAIL STATUS:",i[3])
                
                count+=1
        if count==0:
                print("SORRY, this book is not in the library")


                
def removebook():
        bid=input("Enter bookid u want to delete")
        mycur.execute("select * from bookdetails")
        count=0
        for i in mycur:
                
            if i[0]==int(bid):
                    
                c="delete from book_records where Bookid="+bid
                b="delete from bookdetails where Bookid="+bid
                mycur.execute(c)
                mycur.execute(b)
                mydb.commit()
                print("This book record has been successfully been deleted")
                count+=1
                
        if count==0:
            print("Sorry this book is not in the library")
#ishita





