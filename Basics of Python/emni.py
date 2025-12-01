#1**1 + 2**2 + 3**3 +... + n**n
# def compute_series(n):
#     total = 0
#     for i in range(1, n+1 ): #i starts with a value of 1 and it increases everytime the loop runs.
#         total += i**i #total = total+i**i
#     return total

# # Example usage
# n = int(input("Enter the value of n: "))
# result = compute_series(n)
# print(f"The result of the series for n = {n} is: {result}")

# n = int(input("Enter the value of n: "))
# total = 0
# i = 1

# while i <= n:
#     total += i ** i  # Add i^i to the total
#     i += 1  # Increment i

# print(f"The result of the series for n = {n} is: {total}")

n = int(input("input a number: "))
if(n%2 != 0):
    print("Weird")
if(n%2 == 0 and (n>=2 and n<=5)):
    print("Not Weird")
if(n%2 == 0 and (n>=6 and n<=20)):
    print("weird")
if(n%2 == 0 and n>20):
    print("Not Weird")
    

