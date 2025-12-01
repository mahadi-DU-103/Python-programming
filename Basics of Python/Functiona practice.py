#1. write a function to print the length of a list.(list is the parameter)
homies = ['ashiq', 'ramjan', 'hasib', 'shosso']
bois = ['orin', 'fariba', 'lamha', 'samiha', 'tajvita', 'rimi']
def list_len(list):
    print(len(list))
list_len(bois)

#2.write a function to print the elements of a list in a single line.(list is the parameter)
homies = ['ashiq', 'ramjan', 'hasib', 'shosso']
bois = ['orin', 'fariba', 'lamha', 'samiha', 'tajvita', 'rimi'] 
def list_el(list):
    for item in list:
        print(item, end=" ")
list_el(bois)
list_el(homies)

#3. write a function to find the factorial of n.(n is the parameter)
n = int(input('factorial of which number?'))

def calc_factorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    print(factorial)
calc_factorial(n)

#4. write a function to convert USD to BDT.
n = float(input("how much dollar into BDT?"))
def currency_converter(n):
    BDT = n * 126
    print(n , "USD =", BDT , "BDT")
currency_converter(n)

#5. write a function to chech if a number is even or odd.
n = int(input("input a number:"))
def num_checker(n):
    if(n%2 == 0):
        print("this number is even.")
    else:
        print("this number is odd.")
num_checker(n)

#6. if a year is a leap year or not.
year = int(input("enter your year:"))
def leap_year(year):
    if((year%4==0 and year%100!=0) or year%400==0):
        print('this is a leap year.')
    else:
        print("not a leap year.")
leap_year(year)

#7.Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), 
#and tax percent (the percentage of the meal price being added as tax) for a meal,
#find and print the meal's total cost. Round the result to the nearest integer.
meal_cost = int(input())
tip = int(input())
tax = int(input())
def costing(meal_cost,tax,tip):
    tip = meal_cost*(tip/100)
    tax = meal_cost*(tax/100)
    meal_cost = meal_cost+tax+tip
    print(round(meal_cost))

(costing(meal_cost,tax,tip))   

#9. checking leap year.
def is_leap(year):
    # A year is a leap year if:
    # 1. It is divisible by 4, and
    # 2. It is NOT divisible by 100 unless it is also divisible by 400.
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True  # Divisible by 400
            else:
                return False  # Divisible by 100 but not by 400
        else:
            return True  # Divisible by 4 but not by 100
    else:
        return False  # Not divisible by 4

# Input and test the function
year = int(input())
print(is_leap(year))