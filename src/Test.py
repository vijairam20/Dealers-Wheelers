import os
import csv
class User:
    name =""
    username =""
    password =""
    def __init__(self,name , username ,password):
        self.name = name
        self.username = username
        self.password = password
    def printDetails(self):
        print("Name :"+self.name)
        print("Usename :"+self.username)
        print("Password :"+self.password)
def init():
    print("Dealers Wheelers")
    print("Amzazon for cars")
    print("1.Login")
    print("2.Create New User")
    print("3.View Offers")
    flag = (int)(input())
    if(flag == 1):
        print("A")
        authenticate()
    elif(flag == 2):
        obj = create_user()
        print("User Created")
        init()
    elif(flag ==3):
        print("C")
#Create of Users
def create_user():
    print("Enter Name :")
    name = input()
    print("Enter Username : ")
    username = input()
    print("Enter Password : ")
    password = input()
    obj = User(name, username, password)
    file = open('user.csv','a',newline='')
    data =[[name,username,password]]
    with file:
        writer = csv.writer(file)
        writer.writerows(data)
    return obj
#Read Users
def authenticate():
    print("Enter Username :")
    username = input()
    print("Enter Password :")
    password = input()
    file = open('user.csv','r',newline='')
    flag = False
    with file:
        reader = csv.reader(file)
        for row in reader:
            user = row[1]
            passw = row[2]
            print(user)
            print(passw)
            if user == username and password == passw :
                print("Login Successful")
                flag = True
            break
    if not flag :
        print("Login Unsuccessful")


#main
init()