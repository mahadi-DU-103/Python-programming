#Write a progam to check if a number entered by the user is odd or even.
#ans: if a number is divided by 2 then it is odd, if not even.
num = int(input("input you number:")) 
if(num%2==0):
    print("your given number is even")
else:
    print("your given number is odd")

#Write a program to find the greates of 3 number entered by the user.
num1 = float(input("enter your first number:"))
num2 = float(input("enter your second number:"))
num3 = float(input("enter your third number:"))

if(num1 > num2 and num1 > num3):
    print("the greatest number is:", num1)
elif(num2 > num3):
    print("the greatest number is:", num2)
else:
    print("the greatest number is:", num3)

#Weite a program to chech if a number is a multiple pf 7 or not.
#if we divide the given number by 7 and the remainder remains 0, the number is amultiple of 7.
seven = int(input("enter you number:"))
if(seven % 7 == 0):
    print("your number is a multiple of seven")
else:
    print("your number is not a multiple of seven")
