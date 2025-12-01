str1= "my name is mahadi. \nI study in University of Dhaka."
print(str1) #here '\n' is an escape sequence.

#concatenation
str2 = "i am 21 years old."
str3 = "it is time i get self sufficient"
str4 = str2 + str3
print(type(str4), str4) 
print(len(str1)) #length of string

#indexing
str = "University of Dhaka"
ch = str[4]
print(ch) 
print(str[0:10]) #slicing
print(str[-18:-10])