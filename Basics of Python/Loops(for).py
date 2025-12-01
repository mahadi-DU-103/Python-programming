nums = [1, 2, 3, 4, 5]
names = ['mahadi', 'awfi', 'suvro'] #these are a list.
tup= (1, 2, 3, 4, 5) #this is a tuple.
for val in nums:
    print(val)
for val in names:
    print(val)
for val in tup:
    print(val)

#we can also print characters seperately.Such as:
name = 'mahadi'
for char in name:
    if ( char == 'd'):
        print('d found')
        break
    print(char)
else:
    print("end") #if we did not use else, end would get printed.

#range function:
for el in range(5): #range(stop)
 print(el) 

for el in range(2, 5): #range(start, stop)
 print(el)

for el in range(1,5,2) : #range(start, stop, step)
 print(el)

#pass statement:
for el in range(10):
   pass
print("we will do it later")