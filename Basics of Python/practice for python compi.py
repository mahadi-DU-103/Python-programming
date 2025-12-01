#1. Given the list: data = [8][10][15][10][20][8][10][15][15], write Python code to compute the mean, median, and mode.
import numpy as np
data = np.array([8, 10, 15, 10, 20, 8, 10, 15, 15])
n = len(data)
sum = 0
for i in range(n):
    sum +=data[i]
sum
print(sum,'sum of the data set.')
mean = sum/n
print(mean,"is the mean of the data set.")

#2. variance and standard deviation.
sum_of_square = 0
for i in range(n):
    nominator = (data[i]-mean)**2
    sum_of_square+=nominator
var=sum_of_square/(n-1)
print(var,"is the variance 0f the dataset")
SD = var**0.5
print(SD,"is the standard deviation.")

#3. write a python function that takes n number of coin tosses and return the probability of getting exactly half head.
def prob():
    import math as m
    n = int(input("enter the number of trials: "))
    x = n//2 
    diff = n-x
    """The double divide (//) in Python is used for integer division, which discards the decimal part and always returns a whole number. 
The single divide produces a float even if both operands are int."""
    def facto(num):
        f = 1
        for i in range(1,num+1):
            f*=i
        return f
    comb = facto(n)/(facto(x)*facto(diff))
    print("(nCx)=",comb)
    prob = comb*((0.5)**x)*((1-0.5)**(n-x))
    print(f"X follows binomial(n={n},p=0.5 and the pmf is\n(nCx)*p^{x}*(1-p)^(1-{x}))")
    print("the probability of getting exactlly half head is: ",prob)
prob()

# 4. write a python code called series_identifier that determines whether a given numeric sequence is arithmetic, geometric or neither.
def series_identifier():
    series = np.array(list(map(int,input("enter your series: ").split())))
    n = len(series)
    d = []
    r = []
    for i in range(n-1):
        diff = series[i+1]-series[i]
        ratio = series[i+1]/series[i]
        d.append(diff) 
        r.append(ratio)
        """numbers = [1, 2, 3];
           numbers.append(4);
           print(numbers)   # Output: [1, 2, 3, 4]"""
    is_arithmatic = True
    for i in range(1,n-1):
        if d[i] != d[0]:
            is_arithmatic = False
            break
    is_geometric = True
    for i in range(1,n-1):
        if r[i]!=r[0]:
            is_geometric = False
            break
    if is_arithmatic:
        print("Arithmatic series.")
    elif is_geometric:
        print("Geometric series.")
    else:
        print("Neither geometric nor arithmatic.")
series_identifier()

def series_identifier():
    series = np.array(list(map(int,input("Enter your series: ").split())))
    n = len(series)
    d = []
    r = []
    i = 0
    while i < n-1:
        d.append(int(series[i + 1] - series[i]))             # Convert to int for clean output
        r.append(float(series[i + 1] / series[i]))         # Convert to float for clean output
        i+=1
    print("the common diff are:",d)
    print("the common ratio is:",r)
    i = 1
    is_arithmatic = True
    while i <= (len(d)-1):
        if d[i]!=d[0]:
            is_arithmatic = False
            break
        i+=1
    is_geometric = True
    i = 1
    while i < (len(r)):
        if r[i]!=r[0]:
            is_geometric=False
            break
        i+=1
    if is_arithmatic:
        print("Arithmatic series.")
    elif is_geometric:
        print("Geometric series.")
    else:
        print("Neither geometric nor arithmatic.")
series_identifier()

#5. """write a python program rel_finder that determines the nature and strength of the relations
#between two quantitative variable of arbitrary length n.
# use both while and for loop within the code to achieve this.
# use two vector say x = 5,8,3,10 and y = 3.8,3.5,4,3 to verify whether your rel_finder works or not.""'
    
        



