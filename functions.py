import sqlite3
from sqlite3 import OperationalError


'''Creating resuable functions '''

def ownerManages(cursor, connection):
    while(True):
        print("What would you like to do today? ")
        print("\t1. Add books\n\t2. Remove books\n\t3. Show reports\n\t4. Exit")
        choice = input("Enter 1/2/3/4 : ")
        if choice == '1':
            print("Enter the details of the book you want to add.")
            isbn = input("ISBN of the book : ")
            title = input("Title of the book : ")
            author = input("Author of the book : ")
            price = input("Price of the book : ")
            sale = input("Sale percentage of the book that goes to the publisher : ")
            pages = input("Number of pages of the book : ")
            genre = input("Genre of the book : ")
            print("Is this book published by an \n\t1. Existing Publisher\n\t2. New Publisher")
            p = input("Enter 1/2 : ")
            if p == '1':
                pID = input("Enter Publisher ID : ")
            elif p == '2':
                pID = cursor.execute("SELECT max(publisherID) FROM Publishers;")
                pID = int(pID.fetchall()[0][0])+1
                pID = str(pID)
                pName = input("Enter publisher's name : ")
                pAddress = input("Enter publisher's address : ")
                pPhone = input("Enter publisher's phone number : ")
                pMail = input("Enter publisher's email id : ")
                pbank = input("Enter publisher's bank account number : ")

                print("Thank you for this information! Adding new Publisher . . ")
                a = cursor.execute("INSERT INTO Publishers values(\""+pID+"\",\""+pName+"\", \""+pAddress+"\", \""+pPhone+"\",\""+pMail+"\",\""+pbank+"\");")
                connection.commit()
                print("New publisher added successfully! ")
            
            print("Adding new book to the bookstore . . . ")
            a = cursor.execute("INSERT INTO Books values(\""+isbn+"\", \""+title+"\", \""+author+"\", "+str(price)+", "+str(sale)+", "+str(pages)+", \""+genre+"\", \""+pID+"\");")
            connection.commit()
            print("Book added successfully!")

        elif choice == '2':
            isbn = input("Enter the ISBN of the book you want to remove : ")
            a = cursor.execute("DELETE FROM Books WHERE ISBN = \""+isbn+"\";")
            connection.commit()
            print("Book deleted sucessfully!")

        elif choice =='3':
            sales = cursor.execute("SELECT o.ISBN, max(orderQuantity*price) FROM Books b LEFT OUTER JOIN Orders o GROUP BY o.ISBN;")
            sales = sales.fetchall()
            expen = cursor.execute("SELECT o.ISBN, max(salePercentage*orderQuantity*price/100) FROM Books b LEFT OUTER JOIN Orders o GROUP BY o.ISBN;")
            print(sales)
            expen = expen.fetchall()
            print("-----------")
            print(expen)
            print("This is the sale vs expenditure report for this bookstore.")
            for i in range(len(sales)):
                print("\tBook:\t"+str(sales[i][0])+"\tSale:\t"+str(sales[i][1])+"\tExpenditure:\t"+str(expen[i][1]))
                print()
                #expenditures = cursor.execute("SELECT ISBN, orderQuantity")


        elif choice == '4':
            break






def displayBooks(collection):
    print("--------------------------------------------------------------------------------------------------")
    for book in collection:            
        print("\tTitle     : "+ book[1])
        print("\tISBN      : "+book[0])
        print("\tAuthor    : "+book[2])
        print("\tPrice     : $"+str(book[3]))
        print("\tGenre     : "+book[4])
        print("-----------------------------------------------------------------------------------------------")

def userStarts(user, cursor, con):
    while(True):
        print("What would you like to do today? ")
        print("\t1. Browse all books\n\t2. Search for specific book(s)\n\t3. Place an order\n\t4. Track an Order\n\t5. Exit")
        num = input("Enter 1/2/3/4/5 : ")
        if num =="1":
            print("Here are all books in our store! Currently we do not have a big selection\nbut we are working on it!")
            books = cursor.execute("SELECT ISBN, BookName, author, price, genre FROM Books")
            books = books.fetchall()
            displayBooks(books)
        

        # print(len(books))
        elif num == "2":
            print("What would you like to search by?")
            print("\t1. Book title\n\t2. Author\n\t3. Genre\n\t4. ISBN")
            option = input("Enter 1/2/3/4 :  ")
            if option == '1':
                title = input("Enter full/partial book title : ")
                books = cursor.execute("SELECT ISBN, BookName, author, price, genre FROM Books WHERE BookName LIKE \"%"+title+"%\";")
                books = books.fetchall()
                if(len(books)==0):
                    print("Sorry! No results match your search criteria. ")
                else:
                    displayBooks(books)
            elif option =='2':
                title = input("enter full/partial Author name : ")
                books = cursor.execute("SELECT ISBN, BookName, author, price, genre FROM Books WHERE author LIKE \"%"+title+"%\";")
                books = books.fetchall()
                if(len(books)==0):
                    print("Sorry! No results match your search criteria. ")
                else:
                    displayBooks(books)
            elif option =='3':
                g = cursor.execute("SELECT DISTINCT genre FROM Books;")
                g = g.fetchall()
                print("The available genres are : ")
                for genre in g:
                    print(genre[0], end=", ")
                title = input("\nenter genre : ")
                books = cursor.execute("SELECT ISBN, BookName, author, price, genre FROM Books WHERE genre = \""+title+"\";")
                books = books.fetchall()
                if(len(books)==0):
                    print("Sorry! No results match your search criteria. ")
                else:
                    displayBooks(books)
            elif option =='4':
                title = input("enter full/partial ISBN : ")
                books = cursor.execute("SELECT ISBN, BookName, author, price, genre FROM Books WHERE ISBN LIKE \"%"+title+"%\";")
                books = books.fetchall()
                if(len(books)==0):
                    print("Sorry! No results match your search criteria. ")
                else:
                    displayBooks(books)
            
            else:
                print("you did not enter a valid menu option. Exiting the application now. ")

        elif num == '3':
            r = cursor.execute("SELECT * FROM Orders;")
            #print(r.fetchall())
            print("You have decided to place an order! Let's get the process started.")
            date = input("Enter today's date in EXACTLY YYYY-MM-DD format : ")
            b_delivery = input("Would you like to use the same billing address as enetered during registration? (y/n) ")
            if b_delivery=='y':
                billing = cursor.execute("SELECT billingInfo from Billing where username = \""+user+"\";")
                billing = billing.fetchall()[0][0]
            else:
                billing = input("Enter new billing address : ")
                r = cursor.execute("INSERT INTO Billing values(\""+user+"\",\""+billing+"\");")
                con.commit()

            s_delivery = input("Would you like to use the same shipping address as enetered during registration? (y/n) ")
            if s_delivery=='y':
                shipping = cursor.execute("SELECT shippingInfo from Shipping where username = \""+user+"\";")
                shipping = shipping.fetchall()[0][0]
            else:
                shipping = input("Enter new shipping address : ")
                r = cursor.execute("INSERT INTO Shipping values(\""+user+"\",\""+billing+"\");")
                con.commit()


            
            orders = cursor.execute("SELECT max(orderNum) FROM Orders;")
            maxOrder = orders.fetchone()[0]
            if maxOrder is None:
                orderNum = 00
            else:
                orderNum = int(maxOrder)+1
            diffBooks = int(input("How many DIFFERENT books would you like to add? "))
            for i in range(diffBooks):
                while True:
                    isbn = input("Enter EXACT ISBN of the "+str(i+1)+"th book : ")
                    b = cursor.execute("SELECT * FROM Books WHERE ISBN = \""+isbn+"\";")
                    if (len(b.fetchall())) == 0:
                        print("This ISBN does not exist. Please enter a valid one. ")
                    else: 
                        break
                quantity = (input("Enter how many COPIES of this book do you want? "))
              
                
                print("We have all the required information! Placing the order for this book now!")
                
                cursor.execute("INSERT INTO Orders values("+str(orderNum)+", \'"+str(date)+"\', "+quantity+", "+isbn+", \""+user+"\");")
                con.commit()
                print("\n Order placed Siccessfully! The order number is "+str(orderNum)+" for tracking purposes! ")
                c = cursor.execute("SELECT * FROM ORDERS;")
                #print(c.fetchall())
            #FIX DATE
                
        elif num == '4':
            on = input("Enter the EXACT order number for your username : ")
            orders = cursor.execute("SELECT orderDate, ISBN, orderQuantity FROM Orders WHERE orderNum ="+on+" AND username = \""+user+"\";")
            orders = (orders.fetchall())
            for order in orders:
                print("Your order was made on : "+ str(order[0]))
                print("You ordered "+str(order[2])+" copies of the book with ISBN "+order[1]+" .")
                print("Your order is expected to arrive with 12-15 days of the shipment date.")
            


        elif num == '5':
            break        

       




def executeScriptsFromFile(filename, cursor, connection):
    '''opens a file, reads and stores its contents and closes the file, returns the file contents'''
    f = open(filename, 'r')
    file = f.read()
    print("...processing ")
    
    
    sqlCommands = file.split(';')

    # Execute every command from the input file
    for command in sqlCommands:
        # This will skip and report errors
        # For example, if the tables do not yet exist, this will skip over
        # the DROP TABLE commands
        try:
            cursor.execute(command)
            connection.commit()
        except OperationalError:
            print("Command skipped: ")

    f.close()
    return True