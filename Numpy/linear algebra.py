# # 1. matrix multiplication:
# import numpy as np
# m = np.array([[1,1],[0,1]])
# m1 = np.array([[1,2],[3,4]])
# print(f'first matrix is{m}\nsecond matrix is{m1}')
# dot_mul = np.dot(m,m1)
# cross_mul1 = np.cross(m,m1)
# cross_mul2 = np.cross(m1,m)
# print(f'the dot product is{dot_mul}\nand the cross product is{cross_mul1} and {cross_mul2}')
# # 2. determinant: 
# det = np.linalg.det(m1)
# print(det,"is the determinant of the matrix.")

# def determinant(matrix): # we are using gaussian elimination. determinant = product of diagonal values.
#     n = len(matrix)
#     det = 1 #initial determinant = 1
#     for i in range(n):
#         pivot = matrix[i][i] #pivot hobe 1*1th element or 2*2 or n*n and onwards.
#         if pivot == 0:
#             #pivot 0 hole porer row er sathe swap korbo 
#             for j in range(i+1,n):
#                 if matrix[j][i]!=0: 
#                     matrix[i],matrix[j] = matrix[j],matrix[i] 
#                     #matrix [j] is a row below matrix [i] row
#                     det *= -1 #row swap korar karone sign change hoy
#                     pivot = matrix[i][i]
#                     break # jokhon non zero peye gelo tokhon swap kore loop theke ber hoye jabe break er karone.   
#             else: 
#                 print('the determinant is 0.') # jodi kono non-zero pivot thake tahole determinant 0.
#         det *= pivot
#         #ebar pivot er nicher gulo 0 korbo
#         for j in range(i+1,n): #kaj ta amra pivot er porer row te kortesi.
#             if matrix[j][i] != 0:
#                 factor = matrix[j][i] / pivot
#                 for k in range(i,n): # k is the column index.
#                     matrix[j][k] -= factor * matrix[i][k] #row operation
#     print('the determinant of the matrix is:',det)
# matrix = [[1,2,3],[4,555,6],[7,8,9]]
# determinant(matrix)

# # 3. eigen values and vector:
# w,v = np.linalg.eig(m1)
# print(f'the eigen value of the vatrix is {w}\nand the eigen vector of the matrix is{v}')

"""4.a python code which takes a general m*m matrix as its input and return the sum of the non-diagonal even numbers as its output.
also return how many numbers included in your sum."""
import numpy as np
# def sed2():
#     m = int(input("enter the size of the matrix (m): "))
#     print((f"enter the {m*m} coefficients of the matrix row-wise: "))
#     u = np.array(list(map(int,input().split()))).reshape(m,m)
#     dim = u.shape
#     print("the dimension of the matrix is",dim)
#     total = 0
#     row = dim[0]
#     column = dim[1]
#     count = 0
#     for i in range(row):
#         for j in range (column):
#             if i!=j and u[i,j]%2==0:
#                 total+=u[i,j]
#                 count+=1
#     print(f"the matrix is:\n{u}")
#     print(f'the sum of the non-diagonal values are {total}')
#     print(f'total number added:{count}')
# sed2()  

"""write a python code named sys_solver which takes a general m*m matrix and a vector
of length m as its input and return the solution of a system of linear equation."""
def sys_solver():
    n = int(input("Enter the size of the matrix (n): "))
    print(f"Enter the {n*n} coefficients of matrix A row-wise:")
    A = np.array(list(map(float, input().split()))).reshape(n, n)
    print(f"Enter the {n} constants for vector b:")
    b = np.array(list(map(float, input().split()))).reshape(n,1)

    D = np.linalg.det(A)   #np.linalg.det(A) built in.
    if D == 0:
        print("This system of linear equation is inconsistent hence it has no solution.")
        return
    elif D!=0:
        Dx = A.copy() # makes a copy of matrix A so i dont modify the original.
        Dx[:,0]=b #it targets the first column of Dx and replaces with b.
        Dy = A.copy()
        Dy[:,1]=b #targets the second column of Dy and replaces with vector b.
        x = np.linalg.det(Dx)/D
        y = np.linalg.det(Dy)/D
    print(f'the value of x is  {x}')
    print(f'the value of y is {y}')   
sys_solver()
    
def detrm():
    d = int(input("enter the dimension of the matrix: "))
    v = np.array(list(map(int,input(f"enter {d*d} elements for matrix v: ").split()))).reshape(d,d)
    if d==2:
        D = v[0,0]*v[1,1]-v[0,1]*v[1,0]
    elif d==3:
        D = v[0,0]*(v[1,1]*v[2,2]-v[1,2]*v[2,1])-v[0,1]*(v[1,0]*v[2,2]-v[1,2]*v[2,0])+v[0,2]*(v[1,0]*v[2,1]-v[1,1]*v[2,0])
    else:
        D = np.linalg.det(v)
    print(v)
    print(f'determinant is {D}')
detrm()










