import numpy as np

# #numpy array attributes in python:
#1. ndim (dimension): shows the nuber of dimensions in the array.
lst1 = [10,20,30,40,50]
lst2 = [[1,2,3,4,5],[1,3,5,7,9]]
array1 = np.array(lst1)
array2 = np.array(lst2)
print("the dimension of this array1 is:",array1.ndim)
print("the dimension of array2 is:",array2.ndim)
list1 = np.array([1,2,3,4,5],) #a homogenous list.
list2 = np.array([1,2,3.69,4,5]) #list with a float which is not homogenous.
list3 = np.array([1,2,"3",4,5]) #list with a string value.
list4 = np.array([69.69,96.96], dtype = str) #this is a list with float values.
list5 = np.array([[1,2,3],[4,5,6],[7,8,9]]) #this is a nested list with columns.
list6 = np.arange(1,8) #1D array from 1 to 7.
list7 = np.arange(1,9).reshape(4,2) #this is a matrix having numbers 1-8 as elements where there will be 4 rows and 2 columns.
list8 = np.zeros(6).reshape(3,2) #a 3by2 zero matrix.
list9 = np.ones(4) #a 1by1 1 matrix
print(list1) #this will return a normal list
print(list2) #this will return a all float value list automatically.
print(list3) #this will return a all string value list automatically.
print(list4) #this will return a all string list despite being a float list due to instruction.
print(list5) #this will print a 3by3 matrix.
print(list6)
print(list7)
print(list8)
print(list9)

#2. shape: represents the structure of the array in terms of row and column.
lst3 = [1,2,3,4]
array3 = np.array(lst3).reshape(2,2)
print("matrix of array3 is:",array3)
print("dimension of array3 is:",array3.ndim)
print("shape of array3 is:",array3.shape)

#3. size: indicates total number of elements in the array.
print("the size of array3 is:",array3.size)

#4. dtype(data type): shows the type of data stored in the array.   
print(array3.dtype) #will return the data type and how many bits of data it carries.   

#5. item size: shows memory allocated for each symbol.
print(array3.itemsize)

# indexing in numpy:
array69 = np.array([10,20,30,40,50])
print(array69[2]) #starts counting from 0 when from the left side.
print(array69[-1]) #start counting from -1 when from thee right side]
array96 = np.array([[1,2,3],[4,5,6]]).reshape(2,3)
print(array96)
print(array96[0,1]) #will return element of 1st row and second column.
print(array96[:,2]) #will return all elements of column.

# slicing: slicing is a way to extract a subset of data from numpy array.
arr = np.array([1,2,3,4,5,6,7])
print(arr[1:3]) #returns 2nd element to 3rd element.
print(arr[1:6:2]) #returns 2nd to 5th element with 2 steps.
print(arr[-1:-3:-1]) #returns 1st to 2nd element from the left.
print(arr[::2]) #returns all with 2 steps.
print(arr[::-1]) #returns all from the left side.

arr2d = np.array([[15,16,17],[25,26,27],[35,36,37],[45,46,47]]) 
"""here 15,16,17 are in row number 0; 25,26,27 are in row number 1;
35,36,37 are in row number 2; 45,46,47 are in row number 3."""
print(arr2d[1,]) #will return every element of 2nd row.
print(arr2d[:,1]) #it will return 2nd column which 16,26,36,46.
print(arr2d[1:3,1:3]) #=(row range,column range).
print(arr2d[1:3,]) #this will return 2nd and 3rd of each column.
print(arr2d[:,1:3]) #this will return 2nd and 3rd column of each row.
print(arr2d[1:3,1]) #this will return 2nd column from 2nd to 3rd row.
print(arr2d[1:3,:1]) #this will retur 2nd column from 2nd and 3rd row.


