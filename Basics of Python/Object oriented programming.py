#Casses and Objects in python:
class student:
    name = "mahadi" #this a class.

s1 = student() #and this is an object.
print(s1.name)

class car:
    colour = "blue"
    brand = "GTR"

car1 = car()
print(car1.brand ,car1.colour)

#constructor:
class student1:
    def __init__(self): #default constructors 
        pass
    def __init__(self,surname): #parameterized constructors
        self.name = surname
        print("adding new students in database")
s = student1("pranto")
print(s.name) #pranto 

#class and instances attributes:
class cars:
    car_brand = "nissan" #this is a class attribute
    name = "GTR" #class attribute

    def __init__(self,name,brand):
        self.name = name #object attribute
        self.brand = brand
        print("the best car in the world!")

car1 = cars("nissan", "GTR")
print(car1.name,car1.brand)

#methods
class wel: #classes are defined like this
    def __init__(self,name,uni): #this 
        self.name1 = name
        self.uni = uni #this is a object attribute
    def welcome(self):
        print("i am te king",self.name1,self.uni)
nigga = wel("\npranto", "\nDU") #objects are created like thi
nigga.welcome()


    
         
