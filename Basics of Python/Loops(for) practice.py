#1. print the elements of the following list using for loop, [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for el in num:
    print(el)
#or if automatic:
for el in range(1,11):
    print(el**2)

#2. search for a number x in this tuple using for loop. (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = int(input('what number are you searching in this tuple?'))

index = 0

for el in nums:
    if(el == x):
        print('number found at index', index)
    index += 1
else:
    print("not available.")
#3. print number from 1 to 100:
for el in range(1,101):
    print(el)

#4. print numbers from 100 to 1
for el in range(100, 1, -1):
    print(el)

#5. print the multiplication table of number n:
n = int(input("which multiplication table do you want?"))
for table in range(1, 11):
    print(n * table)

#6. write a program to find the sum of n numbers(using for loops):
n = int(input("enter how many numbers you want to sum? "))
sum = 0
for i in range(1,n+1):
    sum+=i
    print (i)
print(sum)

#7. write a program to find the factorial of first n numbers(use while):
n = int(input('which factorial do you want?'))
factorial = 1

for i in range(1, n+1):
    factorial *= i

print('factorial is:', factorial)

#8. The provided code stub reads and integer,n, from STDIN. For all non-negative integers i<n, print i**2.
n = int(input("enter limit:"))
for i in range(n):
    print(i**2)

#9. Without using any string methods, try to print the following:  123...n
n = int(input())
if(n<=150 and n>=1):
    for i in range(1, n+1):
          print(i,end="")
else:
    print('none')

#10. a code to determine the sum of first odd n numbers:
n = int(input("enter how many numbers you want to sum? "))
sum_odd = 0
for odd in range(1,2**n,2):
    sum_odd+=i
    print (odd)
print(sum)

# 11. a code to determine the sum of first even n numbers:
n = int(input("enter how many even numbers you want to sum: "))
sum_even = 0
for even in range (0,2*n+1,2):
    sum_even +=even
print(even)
print("the sum of",n,"even numbers is: ",sum_even)

n = int(input("anything"))
sum = 0
for i in range(n+1):
    if(i%2==0):
        sum +=i
print(sum)

#12. ncr and npr code:
n = int(input("enter the value of n:"))
r = int(input("enter the value of r:"))
z = n-r
n_fact = 1
r_fact = 1
z_fact = 1
for i in range(n,0,-1):
    n_fact *= i
print(n_fact,f"is the value of {n}!")
for i in range(r,0,-1):
    r_fact *= i
print(r_fact,f"is the value of {r}!")
for i in range(z,0,-1):
    z_fact *= i
print(f"{z_fact} is the value of {z}!")
ncr = (n_fact)/(r_fact*z_fact)
npr = n_fact/z_fact
print(f"the value of ncr is: {ncr}")
print(f"the value of npr is: {npr}")



     