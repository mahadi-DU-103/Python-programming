#checking if a triangle is a right angle tringle or not
a1 = int(input("input x1:"))
b1 = int(input("input x2:"))
c1 = int(input("input x3:"))
a2 = int(input("input y1:"))
b2 = int(input("input y2:"))
c2 = int(input("input y3:"))
d1 = ((a1 - b1)**2 + (a2 - b2)**2)**.5
d2 = ((b1 - c1)**2 + (b2 - c2)**2)**.5
d3 = ((a1 - c1)**2 + (a2 - c2)**2)**.5
if(d1**2 + d2**2 == d3**2):
    print("this is a rightanglr triangle")
elif(d2**2 + d3**2 == d1**2):
    print("this is a rightanglr triangle")
elif(d1**2 + d3**2 == d2**2):
    print("this is a rightangle triangle")
else:
    print("this is not a right angle triagle")
