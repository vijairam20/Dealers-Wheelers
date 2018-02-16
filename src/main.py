import os
import sys
import csv
import time
import pickle
from decimal import Decimal
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
CARS = os.path.join(THIS_FOLDER, 'mtcars.csv')
USERS = os.path.join(THIS_FOLDER,'user.csv')
class User:
    def __init__(self,name , username ,password , cars = 0):
        self.name = name
        self.username = username
        self.password = password
        self.car = 0
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
         print("Type         : "+self.type)
         print("Price        : $"+str(self.price*1000))
         print("Milelage     : "+str(self.mpg))
         print("Horse Power  : "+str(self.hp))
         print("Cylinders    : "+str(self.cyl))
         print("Fuel Tank    : "+str(self.ft))
         print("Length       : "+str(self.length))
         print("Width        : "+str(self.width))
         print("Weigth       : "+str(self.weight))
         if self.stock > 0 :
          print("Stock        : "+str(self.stock))
         else :
          print("Stock : Not Available\n")
class Order :
    def __init__(self,car):
        self.car = car

def printHeader() :
    print("\n\n\t\t\t\t\t<<<DEALERS 'N WHEELERS>>>")
    print("\t\t\t\t\t\t\t\t\t\t\t  -Amazon for cars")
def aldreadyExist(types , pos) :
     for i in range(pos) :
        if types[i] == types[pos] :
            return True
     return False
def removeDuplicates(types) :
    Ntypes =[]
    Ntypes.append(types[0])
    i = 1
    while i < len(types) :
        if not (aldreadyExist(types , i)) :
           Ntypes.append(types[i])
        i += 1
    return Ntypes
def getDetails(n , spec ="" , a = 0):
    types = []
    file = open(CARS, "r", newline='')
    if spec == "" :
        with file :
            reader = csv.reader(file)
            for row in reader :
                types.append(row[n])
    else :
        with file :
            reader = csv.reader(file)
            for row in reader :
                if spec == row[a] :
                   types.append(row[n])
    types = removeDuplicates(types)
    return types
def init():
    printHeader()
    print("\n\n\t1.Login")
    print("\n\t2.Create New User")
    print("\n\t3.View Offers")
    print("\n\t4.Exit")
    print("\n\n\tEnter your options:\t")
    flag = (int)(input())
    if(flag == 1):
        u = None
        while  u == None :
            u = authenticate()
        os.system("cls")
        action(u)
    elif(flag == 2):
        os.system("cls")
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
    file = open(USERS,'a',newline='')
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
    file = open(USERS,'r',newline='')
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
def action(u):
    printHeader()
    print("Welcome back "+u.name)
    print("1.Buy")
    print("2.Purchases")
    print("3.View Details")
    print("3.Quit")
    flag =(int)(input())
    if flag == 1 :
        os.system("cls")
        buy()
    elif flag == 3 :
        print("Details")
        u.printDetails()
    elif flag == 4 :
        print("Purchases")
    else :
        init()
def getCars():
    file = open(CARS, 'r', newline='')
    cars = []
    with file:
        reader = csv.reader(file)
        for row in reader :
            cars.append(Car(row[0],row[1],row[2],Decimal(row[3])+Decimal(row[4]),int(row[5]),int(row[6]),Decimal(row[7]),Decimal(row[8]),Decimal(row[9]),Decimal(row[10]),Decimal(row[12]),Decimal(row[13]),int(row[14])))
    return cars
def getManufacturers():
    brands = getDetails(0)
    i = 0
    inp = 0
    c = 1
    while inp == 0 :
        while i < 5 :
            print(str(c) +":" +brands[c-1])
            c += 1
            i += 1
        i = 0
        print("Press NUM for Brand ")
        print("Press 0 for more")
        inp = int(input())

    return brands[inp-1]
def getType(man ="") :
    if not (man == "") :
        types = getDetails(2,man)
    else :
        types = getDetails(2)
    i = 1
    for t in types:
        print(str(i) + ":" + t)
        i+=1
    print("Press NUM for type")
    inp = int(input())
    return types[inp-1]
def getCar(man = "", type ="") :
    file = open(CARS, 'r', newline='')
    cars =[]
    flag_1 = True
    flag_2 = True
    if man == "" :
        flag_1 = False
    if type == "":
        flag_2 =False
    with file :
        reader = csv.reader(file)
        for row in reader :
            if flag_1 and flag_2 :
                if row[0] == man and row[2] == type :
                    cars.append(Car(row[0],row[1],row[2],Decimal(row[3])+Decimal(row[4]),int(row[5]),int(row[6]),Decimal(row[7]),Decimal(row[8]),Decimal(row[9]),Decimal(row[10]),Decimal(row[12]),Decimal(row[13]),int(row[14])))
            elif flag_1 :
                if row[0] == man :
                    cars.append(Car(row[0],row[1],row[2],Decimal(row[3])+Decimal(row[4]),int(row[5]),int(row[6]),Decimal(row[7]),Decimal(row[8]),Decimal(row[9]),Decimal(row[10]),Decimal(row[12]),Decimal(row[13]),int(row[14])))
            elif flag_2 :
                if row[2] == type :
                    cars.append(Car(row[0],row[1],row[2],Decimal(row[3])+Decimal(row[4]),int(row[5]),int(row[6]),Decimal(row[7]),Decimal(row[8]),Decimal(row[9]),Decimal(row[10]),Decimal(row[12]),Decimal(row[13]),int(row[14])))
    return cars
def buy():
    printHeader()
    print("Enter Option")
    print("1.Search parameters :")
    print("2.Sort By parameters :")
    flag = int(input())
    if flag == 1 :
        os.system("cls")
        printHeader()
        print("1.Manufacturer")
        print("2.Type")
        print("3.Both")
        manuf = ""
        Type = ""
        flag = int(input())
        if flag == 1:
            manuf = getManufacturers()
        elif flag == 2:
            Type = getType()
        elif flag ==3 :
            manuf = getManufacturers()
            Type  = getType(manuf)
        cars = getCar(manuf,Type)
        Bcar = getBuyCar(cars)
        os.system("cls")
        print("Bought")
        Bcar.printDetails()
    if flag == 2 :
        os.system("cls")
        printHeader()
        print("Sort By")
        print("1.Price")
        print("2.Mileage")
        print("3.Horse Power")
        print("4.Fueltank")
        flag = int(input())
        params = ["price","mileage","horse power" ,"fueltank"]
        symbols =["$","L/100km","HP","L"]
        if flag :
            printHeader()
            os.system("cls")
            print("By "+params[flag-1])
            cars = getCars()
            cars = sortBy(cars,flag) #Remember to add sort for all parameters
            print("Select:")
            print("1.Ascending")
            print("2.Descending")
            fl = (int)(input())
            if fl == 2 :
                cars.reverse()
            i = 1
            for c in cars :
                if flag == 1 :
                    print(str(i)+":"+c.manuf+"-"+c.model+" $"+str(c.price))
                elif flag == 2 :
                    print(str(i)+":"+c.manuf+"-"+c.model+" "+str(c.mpg)+"L/100km")
                elif flag == 3 :
                    print(str(i)+":"+c.manuf+"-"+c.model+" "+str(c.hp)+"HP")
                elif flag == 4 :
                    print(str(i)+":"+c.manuf+"-"+c.model+" "+str(c.ft)+"L")
                i+=1
def getBuyCar(cars) :
    i = 0
    inp = 0
    c = 1
    while inp == 0:
        while i < 5 and c-1 < len(cars):
            print(str(c) + ":" + cars[c - 1].manuf+"-"+cars[c-1].model)
            c += 1
            i += 1
        i = 0
        print("Press NUM for Car ")
        print("Press 0 for more")
        inp = int(input())
    return cars[inp-1]
def sortBy(cars,param) :
    size = len(cars)
    t = param
    minI = 0
    if param == 1 :
        for i in range(0, size) :
            d = i + 1
            for d in range(d, size) :
                if cars[d].price < cars[minI].price:
                    minI = d
            cars[i], cars[minI] = cars[minI], cars[i]  #  Swapping Two variables
    elif param == 2 :
        for i in range(0, size) :
            d = i + 1
            for d in range(d, size) :
                if cars[d].mpg < cars[minI].mpg:
                    minI = d
            cars[i], cars[minI] = cars[minI], cars[i]  #  Swapping Two variables
    elif t == 3 :
        for i in range(0, size) :
            d = i + 1
            for d in range(d, size) :
                if cars[d].hp < cars[minI].hp:
                    minI = d
            cars[i], cars[minI] = cars[minI], cars[i]  #  Swapping Two variables
    elif t == 4 :
        for i in range(0, size) :
            d = i + 1
            for d in range(d, size) :
                if cars[d].ft < cars[minI].ft:
                    minI = d
            cars[i], cars[minI] = cars[minI], cars[i]  #  Swapping Two variables
    return cars
#main
init()
