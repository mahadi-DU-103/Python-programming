name = input("enter your name:")
print("welcome", name) #will always accept str values.


val = float(input("enter  any value:")) #while using data casting we can assign any kind of data type.
print(type(val), val)

name = str(input("who are you?"))
age = int(input("how old are you?"))
grade = float(input("what is your cgpa?"))
box = float(input("suppose you have a squared shaped box, assume a length and find its are"))
print("name:", name,print(type(name)))
print(age, "years old", print(type(age)))
print("good grades! cgpa is:", grade,
print(grade))
print("area:", box **2)