import numpy as np
x = np.array([[12,11,15],
             [21,25,20],
             [18,27,16]])
y = np.array([1,2,4,69,96,9])[::-1]
y1 = np.sort(x) #this will return a sorted copy along with the row.
y2 = np.sort(x,axis=0) #this will return a sorted copy along the column.
print("sorted along the row",y1)
print("sorted along the column",y2)
y3 = np.argsort(x) #this will retuern the indices(index values) that would sort an array along the row.
y4 = np.argsort(x,axis=0) #same but along the column.
print("sorted index",y3)
print("sorted index but for columns",y4)
#we can also sort: use array name and sort in place
y.sort()
print(y)
#in order print in descending order:
y5 = y[::-1]
print("array in a descending order",y5)