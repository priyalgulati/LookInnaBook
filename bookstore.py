import sqlite3
import functions
from sqlite3 import OperationalError

#creating a database and connecting to it
con = sqlite3.connect("lookinnabook.db")

#declaring a cursor to use on database
c = con.cursor()

#checking if database already exists
try:
    res = c.execute("SELECT * FROM Publishers")
except OperationalError:
    if functions.executeScriptsFromFile("DDL.sql", c, con) == True:
        print("The tables were created successfully!")


    #initialize data
    if functions.executeScriptsFromFile("DML.sql",c, con) == True:
        print("The tables were initialized successfully!\n")



#result = c.execute("SELECT * FROM Publishers")

print("Welcome to Look Inna Book Bookstore !\n")

own = input("Are you the owner? (y/n) ").lower()
if own == 'y':
    username = input("Enter your username (all lowercase) : ")
    password = input("Enter your password (case sensitive) : ")
    confirm = c.execute("SELECT * FROM Users WHERE username = \""+username+"\" AND password = \""+password+"\"")
    if len(confirm.fetchall()) != 0 and username == "admin" and password == "admin":
        print("Welcome admin! You have successfully logged in to the bookstore! \n")
        functions.ownerManages(c, con)

elif own == 'n':
    ans = input("\nAre you a registered user? (y/n) ").lower()
    if(ans == 'y'):
        username = input("Enter your username (all lowercase) : ")
        password = input("Enter your password (case sensitive) : ")
        confirm = c.execute("SELECT * FROM Users WHERE username = \""+username+"\" AND password = \""+password+"\";")
        if len(confirm.fetchall()) != 0:
            print("Welcome "+username+ "! You have successfully logged in to the bookstore! \n")
            functions.userStarts(username, c, con)

    elif ans == 'n':
        ans = input("Would you like to register as a user? (y/n) ").lower()
        if ans == 'y':
            username = input("Enter your username : ")
            password = input("Enter your password : ")
            pass1 = input("Confirm your password : ")
            while password != pass1:
                print("Your passwords did not match. Please enter them again. ")
                password = input("Enter your password : ")
                pass1 = input("Confirm your password : ")
            #print("INSERT INTO Users values(\""+username+"\",\""+password+"\");")
            confirm = c.execute("INSERT INTO Users values(\""+username+"\",\""+password+"\");")
            con.commit()
            #adding billing shipping address
            bill = input("Enter your billing address : ")
            ship = input("Enter your shipping address : ")
            confirm = c.execute("INSERT INTO Billing values(\""+username+"\", \""+bill+"\");")
            con.commit()
            confirm = c.execute("INSERT INTO Shipping values(\""+username+"\", \""+ship+"\");")
            con.commit()
            #confirm = c.execute("SELECT * FROM Users;")
            ##print(confirm.fetchall())
            functions.userStarts(username, c, con)
        elif ans == 'n':
            print("Thank you for using our Look Inna Book online application!")

        else:
            print("you did not enter a valid answer. Exiting the application now. ")
    else:
        print("you did not enter a valid answer. Exiting the application now. ")
else:
    print("Login unsuccessfull. Start the application again. ")



    



























