# def calculate_sum(a, b): #this is called function definition. a and b are parameters.
#     return a + b
#     print(sum)
# sum = calculate_sum(1,3) #function called; arguements.
# print(sum)
# #note: we use functions to remove redundency. 

# #average of 3 numbers:
# def average(a, b, c):
#     avg = ((a+b+c)/3)
#     print(avg)
#     return(avg)
# average(1,4,7)

# #recursive function
# #1. prints n to 1 backwards.
# def show(n):
#     if(n == 0): #this is the base case which decides whether the function should stop or not.
#         return
#     print(n)
#     show(n-1)

# show(5)

#2. returns n!
def fact(n):
    if(n == 0 or n ==1):
        return 1 #because factorial of 1 and 0 is 0.
    else:
        return n* fact(n-1)
print(fact(5))