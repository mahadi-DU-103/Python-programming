# import numpy as np
# v1 = np.array([1,2,3])
# v2 = np.array([4,5,6])
# lengthv1 = np.linalg.norm(v1)
# lengthv2 = np.linalg.norm(v2)
# print("magnitude via built in function of v1:",lengthv1)
# print("magnitude via built in function of v2:",lengthv2)
# dot1 = np.dot(v1,v2)
# cross = np.cross(v1,v2)
# print("bult in dot product:",dot1)
# print("built in cross product:",cross)
# if(dot1 == 0):
#     print("the vectors are orthogonal.")
# else:
#     print("these vectors are not orthogonal")


# #1. vector addition
# import numpy as np
# vec1 = np.arange(1,4)
# vec2 = np.arange(4,7)
# print(vec1,vec2)
# print(vec1+vec2)

# #2. dot product
# dot_product = np.dot(vec1,vec2)
# print(dot_product, ":is the dot product.")

# #3. cross product
# cross_product = np.cross(vec1,vec2)
# print(cross_product,":s the cross product.")

#4. magnitude of a vector
import numpy as np
a1 = int(input("element 1: "))
b1 = int(input("element 2: "))
c1 = int(input("element 3: "))
vecx = np.array([a1,b1,c1])
print(vecx,":is the vector we want to detemine magnitude of.")
mag = ((a1**2+b1**2+c1**2)**0.5)
print(mag)