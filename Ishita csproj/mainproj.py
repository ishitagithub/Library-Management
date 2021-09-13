#ishita
print("========WELCOME TO SCHOOL LIBRARY IN CORPORATION WITH SIKKIM=========")


a='y' or 'Y'
while a=='y' or a=='Y':
   
    print("======================================================")
    print("Enter 1.FROM MANAGEMENT")
    print("Enter 2.STUDENT")
    print("======================================================")
    
    ans=int(input("enter choice-1 or 2:"))


    if ans==1:
        lid="GIS2021"
        password="098lkj"
        i=str(input("enter id"))
        p=str(input("enter password"))
        if i==lid and p==password:
    
    
            print("======================================================")
            print("1. Add Book Record ")
            print("2. Search Book Record")
            print("3. Delete Book Record")
            print("4. Add Student")
            print("5. Remove Student")
            print("6. Search student")
            print("7. Search students with penalty left")
            print("8. Issue Book")
            print("9. Return Book")
            print("10. Pay penalty")
            print("11. Return to main menu")
            print("======================================================")
            choice=int(input("enter choice-1 to 11:"))



#for adding book record
   
            if choice ==1:                 
                from asbook import addbook
                addbook()
                         
           
   

#for searching book record
       
            elif choice==2:                  
                from asbook import searchbook
                searchbook()
                      






#for deleting book record
               
            elif choice==3:
                from asbook import removebook
                removebook()
       





#for adding new student
            elif choice==4:
                from arstud import addstudent
                addstudent()





#for removing student
            elif choice==5:
                from arstud import removestud
                removestud()
                




#for searching student
            elif choice==6:
                from searchstud import searchstud
                searchstud()




                

           

#for searching student with penalty            
            elif choice==7:
                from searchstud import penstud
                penstud()





#for issuing book
            
            elif choice==8:
                from issuebook import issuebook
                issuebook()
            


                


#for returning book
            elif choice==9:
                from returnbook import returnbook
                returnbook()






#for paying penalty
            elif choice==10:
                from returnbook import penalty
                penalty()
            


            elif choice==11:
                
                a="y"



#for coming out or continuing loop
            if choice!=11:
                a=input("do u want to go to main menu again?If yes then reply 'y'")




        else:
            print("Wrong id or password")



                




 #ishita      

#student
                
    if ans==2:
        print("=======================================================")
        print("1. Issued Book Report")
        print("2. Search Book Record")
        print("3. Penalty record")
        print("4. Your account")
        print("5. Return to main menu")
        print("=======================================================")

        choice=int(input("Enter your choice 1-5:"))
   





#for issued book record
            
        if choice==1:
                from report import issuereport
                issuereport()
            





#for searching book record
       
        elif choice==2:                  
            from asbook import searchbook
            searchbook()


                      


#for penalty record
            
        elif choice==3:
            from report import penreport
            penreport()






#for student record
            
        elif choice==4:
            from report import stud
            stud()


            
            

        elif choice==5:
            a="y"
    

#for coming out or continuing loop
        if choice!=5:
            a=input("do u want to go to main menu again?If yes then reply 'y'")
   
   
           
#ishita

