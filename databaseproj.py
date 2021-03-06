# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 18:57:56 2021

@author: Ronish
"""
#student database project by using  sql database
import sqlite3
import csv
import smtplib  #libray for sending email

#create a database
db = sqlite3.connect("DB1.sqlite")

#create a table

try:
    db.execute("""create table student (
                  Roll integer,
                  name text,
                  Math integer,
                  Science integer,
                  Computer integer)""")
except:
    pass



def addStudent():
    print("-------------ADD ANEW STUDENT HERE------------")
    
    list1 = []
    roll = int(input("Enter your roll number: "))
    list1.append(roll)
    n =  input("Enter your name: ")
    list1.append(n)
    m = int(input("Enter your marks in Math: "))
    list1.append(m)
    s = int(input("Enter your marks in Science : "))
    list1.append(s)
    c = int(input("Enter your marks in Computer: "))
    list1.append(c)
    
    db.execute("insert into student values(?,?,?,?,?)",list1)
    db.commit()
    print("----------------NEW STUDENT ADDED--------------------")    
    
def checkPerc():
    print("-------------------Calculate Percentage Here-------------------")
    r = int(input("Enter your roll number to calculate the Percentage: "))
    cursor = db.cursor()
    cursor.execute("select * from student where Roll = ?",[r])
    var = cursor.fetchall()
    print(var)
    print("-"*80)
    print("Roll Number: ",var[0][0])
    print("Name: ",var[0][1])
    print("Math: ",var[0][2])
    print("Science: ",var[0][3])
    print("Computer: ",var[0][4])
    perc = (var[0][2] + var[0][3] + var[0][4])/3
    print("Percentage: %.2f"%perc)
    print("-"*80)
    cursor.close()
    
    
def generateReport():
   
    cursor = db.cursor()
    cursor.execute("select * from student")
    var = cursor.fetchall()
    
    

    #writing data into csv file
    f = open("report.csv" , "w", newline="")  
    obj = csv.writer(f)  
    obj.writerow(["Roll", "Name", "Math","Science","Computer","Perc"])
    
    for item in var:
        perc = (item[2] +item[3]+item[4])/3
        obj.writerow(item+(perc,))
    f.close()
#calculating percentage
 
    print("-"*80)
    print("REPORT GENERATED SUCCESSFULLY")
    print("-"*80)
    cursor.close()
    
def sendReport():    #Sending report card
    s_id = input("Enter student's email id: ")
    server = smtplib.SMTP("smtp.gmail.com",587) #1 server address #2 port number
    server.starttls() # to make a secure connection
    print("Connected with server")
    
    #sending percentage
    r = int(input("Enter your roll number to calculate the Percentage: "))
    cursor = db.cursor()
    cursor.execute("select * from student where Roll = ?",[r])
    var = cursor.fetchall()
    perc = (var[0][2] + var[0][3] + var[0][4])/3
    
    #login
    username = input("Enter your email id: ")
    password= input("Enter your password: ")
    server.login(username,password)
    print("Login Successful")
    
    #send an email
    msg  =""" \ Subject: Report card Percentage: %.2f""" %perc
    server.sendmail(username,s_id,msg)
    print("Mail sent successfully")
    
      
    
    
while True:
    print("_______________MAIN MENU___________")
    print("1. Add a New student\n2. Check Percentage\n3. Generate Report in CSV Format\n4. Send Report\n5 Exit")
    ch = int(input("Enter your choice: "))
    
    if ch == 1:
        addStudent()   #function call
        
    elif ch == 2:
        checkPerc()  #funcion call
        
    elif ch == 3:
        generateReport()    #funcion call
        
    elif ch == 4:           #function call
        sendReport()
        
    elif ch == 5:
        print("------BYE--------")
        break
    else:
        print("---------INVALID CHOICE----------")
    
