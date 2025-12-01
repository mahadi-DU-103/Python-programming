num = int(input("input amy number:"))
if(num<2):
    print("greater")
elif(num > 5):
    print("lesser")
else:
    print("invalid")    

num = int(input("any number"))
if(num % 2 == 0):
    print("even")
else:
    print("odd")

a = int(input("any number"))
b = int(input("any number"))
c = int(input("any number"))
if(a>b and a>c):
    print("a is the greatest")
elif(b>c):
    print("b is the greatest")
else:
    print("c is the greatest")
