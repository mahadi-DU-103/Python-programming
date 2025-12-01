import numpy as np
#1.print number from 1 to 100.
num = 1
while num <= 100: #this is a stopping condition.
    print(num)
    num += 1

#2.print numbers from 100 to 1
num = 100
while num >= 1:
    print(num)
    num -=1

#3.print the multiplication table of a number n.
n = int(input("which multiplication table do you want?"))
i = 1
while i<=10:
    print (n,"*", i ,"=", n*i)
    i += 1

#4.print the elements of the following list using the loop.
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx < len(list):
    print(list[idx]) #list[0], list[1], list[2], ...
    idx += 1

#5.Search for a number x in the tuple.
# nums = np.array(list(range(1,100))) #this is called linear search.
# x = int(input("what number are you searching?"))
# i = 0
# while i < len(nums):
#     if(nums[i]==x):    
#         print("number has been found.")
#         break 
#     else:
#         i += 1  # Only increment i if the number is not found.
# if i == len(nums):
#     print("Number not found.")
#.6 write a program to find the factorial of first n numbers(use while):
n = int(input('which factorial do you want?'))
factorial = 1
i = 1
while i <= n:
    factorial*=i
    i +=1
print('factorial of the number is:', factorial)

#6. write a program to determine summition of (1/x to the power p):
x = 1
n = int(input("enter the value of how many times you want to sum: "))
p = float(input("enter the desired power: "))
sum = 0
while x<=n :
    sum = sum + (1/x**p)
    x+=1
print("the sum of the series of n terms is: ",sum)
if p>1 :
    print("the series is be a converging series.")
else:
    print("the series is be diverging series")

#7. a code to determine the sum of first odd n numbers:
n = int(input("Enter the number of odd numbers to sum: "))

sum_odds = 0  # This will store the sum of odd numbers
current_odd = 1  # The first odd number
count = 0  # Counter for how many odd numbers have been added
while count < n:
    sum_odds += current_odd
    current_odd += 2  # The next odd number
    count += 1
    print(current_odd)

print("The sum of the first", n, "odd numbers is:", sum_odds)

#8. a code to determine the sum of first even numbers:
n = int(input("Enter the number of even numbers to sum: "))
sum_even = 0 #it will will store the total sum of even numbers.
current_even = 0 #it will start at 0 and will go up by 2 each time (to get 0, 2, 4, 6...).
count = 0 #it will track how many even numbers have been added so far.
while count<n:
    sum_even +=current_even
    current_even +=2
    count+=1
    print(current_even)
print("The sum of first",n,"even numbers is: ",sum_even)

#9. write a python code called series_identifier that determines whether a given numeric sequence is arithmetic, geometric or neither.
def series_identifier():
    series = np.array(list(map(int,input("Enter your series: ").split())))
    n - len(series)
    d = []
    r = []
    
    i = 0
    while i <= n-1:
        diff = series[i+1]-series[i]
        ratio = series[i+1]/series[i]
        i+=1
        d.append(diff)
        r.append(ratio)
    print("the common diff are:",d)
    print("the common ratio is:",r)

    is_arithmatic = True
    while i <= (n-1):
        if d[i]!=d[0]:
            is_arithmatic = False
            i+=1
            break
    is_geometric = True
    while i < (n-1):
        if r[i]!=r[0]:
            is_geometric=False
            i+=1
            break
    if is_arithmatic:
        print("Arithmatic series.")
    elif is_geometric:
        print("Geometric series.")
    else:
        print("Neither geometric nor arithmatic.")
series_identifier()
