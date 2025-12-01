#arithmetic operators
a = 2
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) #we'll get remainder
print(a**b) #a^b

#relational operator
a = 50
b = 40
print(a==b) #false
print(a!=b) #true
print(a>b) #true
print(a<b) #false
print(a>=b) #true
print(a<=b) #false

#assingment operators
num = 20
num %= 10 #(+=, -=, *=, /=, **)
print('num2 is :', num)

#logical operators
a = 20
b = 40
print( not False)
print(not a>b) #a>b is false
print("summition is :", a or b)
print("multiplication is :", a and b)
print('OR operator :', (a==b) or (b > a))
print('AND operator :', (b/a) and (a/b))