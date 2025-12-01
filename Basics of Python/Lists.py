marks = [10, 11, 14, 15, 17] #o, 1, 2, 3, 4, 5...nth value.
print(marks)
print(type(marks))
print(len(marks)) #length of list.
print(marks[3])

#we can also store multiple types of data together.
mahadi = ["Statistics, University of Dhaka", 3.88] #dept, uni, cgpa
mahadi[0]= "department of statistics" #lists are changable
print (mahadi)

#list slicing
mahadi = [1, 2 , 3, 4, 5]
print(mahadi[1:4])
print(mahadi[-3:-1])

#list methods
list = [3,2,1,4]
list.append(0) #adds elements at te end.
print(list)

list.sort()
print(list) #sorts in ascending order.

list.sort(reverse=True) #list.reverse() does the same job.
print(list) #sorts in descending order.

list.insert(0,100)
print(list) #inserts elements at index.

list.pop(3)
print(list) #removes element at the specified position.

list.remove(1)
print(list) #removes firt occurence of elements. 

list.extend([2,4]) #adds the specified list elements to the end of the current list.
print(list)

print(list.count(2)) #returns the number of elements with the specified value.

b=list.copy()
print(b)

list.clear() #removes all the elements from a list.
print(list)