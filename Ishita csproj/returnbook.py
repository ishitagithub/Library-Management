#ishita
import mysql.connector
mydb=mysql.connector.connect(user='root',
                                 host='localhost',
                                 password='Ishita.mysql')
mycur=mydb.cursor(buffered=True)
mycur.execute("use library")


def date():
    import datetime
    d=datetime.datetime.now
    return (d().date())




#ishita
def returnbook():
       
        ad=int(input("enter your admnno"))
        mycur.execute("select * from students")
        count=0
        c=0
        for i in mycur:
            # for checking whether name of student is there
            if i[0]==ad:
                print(i[1])
                bid=int(input("Enter bookid u want to return"))
                iid=int(input("Enter issue id"))
                mycur.execute("select * from bookdetails")
                count+=1
                for i in mycur:
                    if i[0]==bid and i[3]=='no':
                        return_date=date()



                        #PENALTY CONCEPT
                        import datetime
                        mycur.execute(("select * from book_records where issue_id=%s"),(iid,))
                        penalty=0
                        
                        for i in mycur:
                            d=i[2]
                            


                            rdate=d+datetime.timedelta(days=7)



                            if return_date>rdate:
                                rd=return_date-rdate
                                day=rd.days
    
                                penalty=day*10



    
        
                            mycur.execute("select * from book_records")
                            if i[1]==bid:
                                
                            #using book_records table
                                
                                if penalty==0:
                                    v=("update book_records set return_date =%s where bookid =%s")
                                    mycur.execute(v,(return_date,bid))
                                    mydb.commit()
                                    print("You have successfully returned the book")
                                    
                                else:
                                    v=("update book_records set return_date =%s,penalty=%s where bookid =%s")
                                    mycur.execute(v,(return_date,penalty,bid))
                                    mydb.commit()
                                    m=("update students set penalty=%s where admn_no=%s")
                                    mycur.execute(m,(penalty,ad))
                                    print("You have successfully returned the book But You are charged with penalty of ",penalty)


                        
                                up=("update bookdetails set avail_status='yes' where Bookid =%s")
                                t=(bid,)
                                mycur.execute(up,t)
                                mydb.commit()
                                c+=1
                                break

        if count==0:
            print("YOUR NAME IS NOT THERE IN STUDENT RECORDS ONLY,HOW CAN YOU RETURN A BOOK??")
        if c==0:
            print("You have not issued the book")




#made by ishita
            
def penalty():
    ad=int(input("enter your admnno"))
    mycur.execute("select * from students")
    mycur.execute("select * from students where penalty is not null")
    c=0
    for i in mycur:
        if i[2]!=0 and i[0]==ad:
            print("Pay penalty-",i[2])
            a=str(input("Has the penalty been paid, write y for yes and n for no.Only full penalty is accepted"))
            c+=1
            if a=='y' or a=='Y':
            
                m=("update students set penalty=0 where admn_no=%s")
                bm=("update book_records set penalty=0 where admn_no=%s")
                mycur.execute(m,(ad,))
                mycur.execute(bm,(ad,))
                print("penalty successfully paid")
    if c==0:
        print("NO PENALTY")
            
#ishita


