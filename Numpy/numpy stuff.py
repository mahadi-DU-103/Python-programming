
# #mcq evaluation:
# import numpy as np
# A = str(input("answer to the question no A:"))
# B = str(input("answer to the question no B:"))
# C = str(input("answer to the question no C:"))
# D = str(input("answer to the question no D:"))
# E = str(input("answer to the question no E:"))
# submitted_answers = np.array([A,B,C,D,E])
# correct_answers = np.array(['a','b','c','d','a'])
# total_marks = 0
# wrong_answers = 0
# blank = 0
# n = len(submitted_answers)
# for i in range(n):
#     if submitted_answers[i] == correct_answers[i]:
#         total_marks += 1
#     elif submitted_answers[i] == '':
#         blank += 1
#     elif submitted_answers[i] != correct_answers[i] and submitted_answers[i]!='':
#         total_marks -= 0.25
#         wrong_answers += 1
#         print(f"wrong answer {submitted_answers[i]} and the correct anwers would be: {correct_answers[i]}")
# print(f'total marks is: {total_marks}\n{wrong_answers} wrong answers were given and\n{blank} were kept blank.')

#correlation
import numpy as np
def rel_finder(x,y):
    sum1 = 0
    sum2 = 0
    ssx = 0
    ssy = 0
    sp = 0
    i = 0
    n = len(x)
    while i < n:
        sum1 += x[i]
        sum2 += y[i]
        i+=1
    am1 = sum1/n
    am2 = sum2/n
    for i in range(n):
        ssx += (x[i]-am1)**2
        ssy += (y[i]-am2)**2
    sp = (x[i]-am1)*(y[i]-am2)
    r = sp/(ssx*ssy)**0.5
    print("correlation is:",r)
    print("correlation coefficient ,r =",r)
    if r<0:
        print("nature of r is -ve")
    if r>0:
        print("nature of r is +ve")
    if r==0:
        print("no relation is exist")
    absolute_r = abs(r)
    if absolute_r<0.5:
        print("correlation is strong")
    if absolute_r>0.5:
        print("correlation is strong")
val1 = list(map(float,input("enter the value of vector x:").split()))
val2 = list(map(float,input("enter the value of vector y:").split()))
x = np.array(val1)
y = np.array(val2)
rel_finder(x,y)
