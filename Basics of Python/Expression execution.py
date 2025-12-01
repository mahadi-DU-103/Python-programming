A,B = 2,3
text = 'CR7'
print(2*text*3) #1.string and numeric values can operate together with '*'.

A,B = '2',3
text = 'CR7'
print((A+text)*B) #2.string and string can operate with '+'.

A,B,C = 2, 3, 4
print(A+B*C) #3.numeric values can operate with all arithmetic operators.

a,b = 2,3.34
print(a*b) 
print(a+b) #4.arithmetic expression with integer and float will result in integer.

a,b = 3,4
print(a/b) #5.result of division operator with two integers will be float.

a,b = 1.5, 4.5
print(a//b)
"""6.integr division with float and int will give int displayed as float:
 ths is a kind of floor,
 which gives closest integer which is lesser than or equal to the float value."""

a,b = -5,2
print(a%b)
print(-a%-b) #7.remainder(vagsesh) is negative when denominator is negative.