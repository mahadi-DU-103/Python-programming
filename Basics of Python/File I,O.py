"""note:
1. open() function takes 2 arguements:
    *the file_path, uch as 'filename.txt'
    *the mode for how to use the file.
2. there are three modes you can open a file with:
    *'r' for reading a file
    *'w' for writing a file-it overwrite existing file content.
    *'a' for writing from the end of a file. adds writing."""



#open, read and close file:
f = open("demo.txt", "r") #r means read only
data = f.read() #reads entire line. 
print(data)

f = open("og", "r")
line2 = f.readline() #reads one line at a time.
print(line2)
print(type(data))
f.close()

f = open("og", "w")
f.write("i want to learn python.") #overwrites the entire file. 
f.closed

f = open("demp.txt", "a")
f.write("\ni am the king") #adds to the file.
f.closed

f = open("faith","r+") #writes and reads the file simultaneously.(no truncate)
f.write("Allah")
print(f.read())
f.closed

with open("faith","r") as f: #with syntax.
    datum = f.read()
    print(datum)

import os
os.remove("demo.txt") #deletes a file.

f = open("file io.txt",'w+')
f.write("i am mahadi.")
f.seek(0) #starts reading from the beginning otherwise pointer shifts stays at the end.
data = f.read()
print(data)
