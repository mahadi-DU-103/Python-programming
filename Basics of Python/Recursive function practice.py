#1. erite a recursive function to calculate the sum of first n natural numbers.
def calc_sum(n):
    if(n == 0):
        return 0
    return calc_sum(n-1) + n

sum = calc_sum(int(input("which natural number?")))
print(sum)

"""2. write a recursive function to print all elements in a list.
      use list and index as parameters."""
def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print(list,idx +1)

bros = ["ashiqXsumaya", "orin,","taj","areeba","hasib","fariba","samiha","lamha","tajvita","rimi","ramjan",]
print_list(bros)
OGS = ["awfi","suvro","sam"]
print_list(OGS)