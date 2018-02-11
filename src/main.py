import os
import sys
import csv
from decimal import Decimal
class User:
    def __init__(self,name , username ,password):
        self.name = name
        self.username = username
        self.password = password
    def printDetails(self):
        print("Name :"+self.name)
        print("Usename :"+self.username)
        print("Password :"+self.password)
class Car:
    def __init__(self,manuf , model, type , price , mpg , cyl , hp , ft , pas , length , width , weight , stock):
        self.manuf = manuf
        self.model = model
        self.type = type
        self.price = price
        self.mpg = mpg
        self.hp = hp
        self.cyl = cyl
        self.ft = ft
        self.pas = pas
        self.length = length
        self.width = width
        self.weight = weight
        self.stock = stock

    def printDetails(self):
         print("Manufacturer : "+self.manuf)
         print("Model        : "+self.model)
         print("Type         :"+self.type)
         print("Price        : $"+str(self.price))
         print("Milelage     : "+str(self.mpg))
         print("Horse Power  : "+str(self.hp))
         print("Cylinders    : "+str(self.cyl))
         print("Fuel Tank    : "+str(self.ft))
         print("Length       : "+str(self.length))
         print("Width        : "+str(self.width))
         print("Weigth       :"+str(self.weight))
         if self.stock > 0 :
          print("Stock : "+str(self.stock))
         else :
          print("Stock : Not Available\n")

def init():
    print("Dealers Wheelers")
    print("Amzazon for cars")
    print("1.Login")
    print("2.Create New User")
    print("3.View Offers")
    print("4.Exit")
    flag = (int)(input())
    if(flag == 1):
        u = authenticate()
        purchase(u)
    elif(flag == 2):
        obj = create_user()
        print("User Created")
        init()
    elif(flag ==3):
        print("C")
    elif(flag == 4):
        print("Quitting")
        os.system('cls')
        sys.exit
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
            if user == username and password == passw :
                print("Login Successful")
                u = User(row[0],row[1],row[2])
                flag = True
                break
        if not flag :
            print("Login Unsuccessful")
            return
    return u
#Purchase
def purchase(u):
    print("Welcome back "+u.name)
    print("1.Buy")
    print("2.Purchases")
    print("3.View Details")
    print("3.Quit")
    flag =(int)(input())
    if flag == 1 :
        print("Search By")
        print("1.Manufacturer")
        print("2.Type")

    elif flag == 3 :
        print("Details")
        u.printDetails()
    elif flag == 4 :
        print("Purchases")
    else :
        init()
def getCars() :
    file = open("src\mtcars.csv",'r',newline='')
    cars = []
    with file :
        reader = csv.reader(file)
        for row in reader :
            cars.append(Car(row[0],row[1],row[2],Decimal(row[3])+Decimal(row[4]),int(row[5]),int(row[6]),Decimal(row[7]),Decimal(row[8]),Decimal(row[9]),Decimal(row[10]),Decimal(row[12]),Decimal(row[13]),int(row[14])))
    return  cars
#main
init()

