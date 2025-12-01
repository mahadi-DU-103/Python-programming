"""1. create a new file "practice.txt" using python. add the following data in it:
Hi everyone 
we are learning File I/O
using Python
I like programming in Python."""

with open("practice","w") as f:
    f.write("Hi everyone \nwe are learning File I/O.")
    f.write("\nusing python\nIlike programming")

#2. write a function that replace all occurences of "python" with "java" in above fie.
def replacement():
   # data = str(input()) , can we not replace with something the user wants?
    with open("practice","r") as f:
        data = f.read()
        new_data = data.replace("python","java")
        print(new_data)
    with open("practice","w") as f:
        f.write(new_data)
replacement()

#3. search if the word "learning" exists in the file or not.
def checking():
    word = str(input("what are you searching?"))
    with open("practice","r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("found")
        else:
            print("not found")
checking()

#4. write a function to find in which line of the file does any word occur first. print whatever i wish if word not found.
def check_for_line():
    word = str(input("anything?")) #were searching this
    data = True #at the beginning the data is true. because for the starting iteration we want to run the loop. otherwise if we start it with an empty string it wont run.
    line_no = 1
    with open("practice.txt", "r") as f:
        while data: #we will read as long as the value of data is not empty.
            data = f.readline()
            if(word in data):
                print(line_no)
            line_no+=1
    return -1
print(check_for_line())

#5. form a file containing numbers seperated by comma, print the count of even numbers.
count = 0
with open("numbers", "r") as f:
    data = f.read()
    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1
print(count) 
"""Whitespace Issues: If there are spaces around the commas in the file (e.g., 1, 2, 3), 
int(val) will raise an error. To handle this, you can strip whitespace from each number:
for val in nums:
    if int(val.strip()) % 2 == 0:
        count += 1"""

