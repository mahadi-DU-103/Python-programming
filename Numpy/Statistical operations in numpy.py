import numpy as np
# import statistics as stat
# x1 = np.array([[1,3,5,7,2]])
# z1 = [1,2,3,4,5]
# y1 = np.max(x1)
# print(y1,"is the maximum value.")
# y2 = np.min(x1)
# print(y2,"is the minimum value.")
# y3 = np.sum(x1)
# print(y3,"is the sum of all elements.")
# y4 = np.mean(x1)
# z2 = stat.mean(z1)
# print(z2)
# print(y4,"is the mean of the elements.")
# y5 = np.median(x1)
# print(y5,"is the median of the elements.")
# y6 = np.prod(x1)
# print(y6,"is the product of all elements.")
# y7 = np.var(x1)
# print(y7,"is the variance of the elements.")
# y8 = np.std(x1)
# print(y8,"is the standard deviation of the elements.")

#manually:
#1. arithmetic mean:
def am(vector):
    sum = 0
    i = 0
    length = len(vector)
    print(length,"is the length of the vector.")
    while i < length:  #for for-loop arguement(for i in range(length):)
        sum += vector[i]
        i+=1
    print(sum,"is the total sum")
    amean = sum/length
    print(amean, "is the arithmetic mean of the vector.")
vector_val = list(map(int,input('enter the elements of the vector: ').split()))
vector = np.array(vector_val)
am(vector)

# 2.geometric mean:
def gm (siu):
    if any(i < 0 for i in siu):
        return print("geometric mean for this data set can't be determined due to the presence of a non-zero value.")
    multiple = 1
    lengm = len(siu)
    i = 0
    print("length of the data set we want determine g-mean of: ",lengm)
    while i < lengm:
        multiple = (multiple)*siu[i]
        print(multiple,f"is the multiple{[i]}'th of the numbers.")
        i+=1
        gmean = multiple ** (1/lengm)
    print(gmean,"is the geometric mean.")
siu_val = list(map(int,input("enter the inputs of the data set: ").split()))
siu = np.array(siu_val)
gm(siu)
import statistics as stat
# g_m = [6,5,4,3,-2,1]
# gmean = stat.geometric_mean(g_m) #to make sure that our program is right.
# print(gmean)

# 3.harmonic mean:
def hm(siuu):
    n1 = len(siuu)
    sum_hm = 0
    i = 0
    print("length when harmonic mean",n1)
    while i<n1:    #while i < n1: ; i+=1
        print(f"{siuu[i]} is the {[i]}'th element of the dataset.")
        sum_hm += 1/siuu[i]
        i+=1
    hmean = n1/(sum_hm)
    print(f"{hmean} is the harmonic mean of the data set.")
siuu_val = list(map(int,input("enter the values of the data set: ").split()))
siuu = np.array(siuu_val)
hm(siuu)

# h_m = list(range(1,10))
# h_mean = stat.harmonic_mean(h_m)
# print(h_mean)

#3. variance
def var(x):
    sum_var = 0
    n = len(x)
    print("length when variance",n)
    for i in range(n):
        sum_var +=x[i]
    print("sum when variance",sum_var)
    mean = sum_var/n
    print(mean,"is the mean.")
    squared_diff_sum = 0
    for i in range(n):
        squared_diff = (x[i] - mean) ** 2
        squared_diff_sum += squared_diff
    variance = squared_diff_sum/(n-1) 
    print("variance is:",variance)
x_val = list(map(int,input("enter the values of the data set: ").split()))
x = np.array(x_val)
var(x)
va_r = list(range(1,11))
print(va_r)
variance1 = stat.variance(x) #unbiased variance(divided by n-1)
print(variance1)    

# # 4. sum of square:
# def ss(w):
#     sum_of_elements = 0
#     sum_of_square = 0
#     n_ss = len(w)
#     print(f"length when sum of square:{n_ss}")
#     for i in range(n_ss):
#         sum_of_elements += w[i]
#         mean_ss = sum_of_elements/n_ss
#         print(f"{w[i]} is the value of the {i}'th element.")
#     print(f"sum of the elements:{sum_of_elements}")    
#     print(f"mean of this data set:{mean_ss}")
#     for i in range(n_ss):
#         sum_of_square += (w[i]-mean_ss)**2
#     print(f"sum of square of this data set is:{sum_of_square}")
# w = list(range(1,11))
# ss(w)

# # 5. sum of product:
# def sop(v1,v2):
#     len_sop1 = len(v1)
#     len_sop2 = len(v2)
#     sum68 = 0
#     sum69 = 0
#     sum_of_pv1 = 0
#     sum_of_pv2 = 0
#     for i in range(len_sop1):      
#         sum68 += v1[i]
#         print(f"{i}th elements of v1 is:{v1[i]}")
#     mean1 = sum68/len_sop1 
#     print(mean1,":is the mean of v1")
#     for i in range(len_sop2):
#         sum69 += v2[i]
#         print(f"{i}th elements of v2 is:{v2[i]}")
#     mean2 = sum69/len_sop2
#     print(mean2,":is the mean of v2")
#     for i in range(len_sop1):
#         sum_of_pv1 += abs(v1[i]-mean1)
#     print(f"sum of product for v1 is:{sum_of_pv1}")
#     for i in range(len_sop2):
#         sum_of_pv2 += abs(v2[i]-mean2)
#     print("sum of product for v2:",sum_of_pv2)
#     sum_of_product = sum_of_pv1*sum_of_pv2
#     print(sum_of_product,":is the sum of product of the data sets.")
# v1 = list(range(1,11,2))
# v2 = list(range(2,11,2))
# sop(v1,v2)

#covariance:
def cov(c1,c2):
    len_c1 = len(c1)
    len_c2 = len(c2)
    sample_size = len(c1+c2)
    tot_c1 = 0
    tot_c2 = 0
    i = 0
    j = 0
    k = 0
    l = 0
    while i < len_c1:
        tot_c1+=c1[i]
        i+=1
        mean_c1 = tot_c1/len_c1
    print(f"Mean of the first data set is: {mean_c1}")
    while j < len_c2:
        tot_c2+=c2[j]
        j+=1
        mean_c2 = tot_c2/len_c2
    print(f"Mean of the second data set: {mean_c2}")
    while k<len_c1:
        sum_diff_c1 = abs(c1[k]-mean_c1)
        k+=1
    print(f"the sum of difference about the mean for the first data set is: {sum_diff_c1}")
    while l<len_c2:
        sum_diff_c2 = abs(c2[l]-mean_c2)
        l+=1
    print(f"the sum of difference about the mean foor the second data set: {sum_diff_c2}")
    sum_of_product = sum_diff_c1*sum_diff_c2
    cova = sum_of_product/(sample_size-1)
    print(f"The covariance of these data sets are: {cova}")
c1_val = list(map(int,input("enter the values of the first data set: ").split()))
c1 = np.array(c1_val)
c2_val = list(map(int,input("enter the values of the second data set: ").split()))
c2 = np.array(c2_val)
cov(c1,c2)




# 7. pearson's correlation co-efficient:
import math as m
import numpy as np
def rel_finder(u1,u2):
    n_u1 = len(u1)
    i=0
    sum_1 = 0 
    sum_2 = 0
    while i< n_u1: # for e jemon ekta loop er under ei shob hoyechilo ekhane hobena cause i keu increament korte hobe jeta for e automatic hoto.
        sum_1+=u1[i]
        sum_2+=u2[i]
        i+=1
    mean1 = sum_1/n_u1
    mean2 = sum_2/n_u1
    xdiff_sq = 0
    ydiff_sq = 0
    sum_of_product = 0
    i = 0
    while i < n_u1:
        xdiff = u1[i]-mean1
        ydiff = u2[i]-mean2
        xdiff_sq += xdiff**2
        ydiff_sq += ydiff**2
        sum_of_product += xdiff*ydiff
        i+=1
    print(f"the sum of product of the data stes is {sum_of_product}")    
    corr_coeff = sum_of_product/m.sqrt(xdiff_sq*ydiff_sq)
    print(f"the correlation coefficient of the 2 variables are {corr_coeff}")
    if corr_coeff>=0.9 or corr_coeff<=-0.9:
        print(f'the 2 variables have very strong linear relationship.')
    elif corr_coeff<=0.1 or corr_coeff>=-0.1:
        print(f'the 2 variables have very weak linear relationship.')
    elif corr_coeff>=0.5 or corr_coeff<=-0.5:
        print("the variables have some what strong relationship.")
    else:
        print("the varibles have somewhat weak linear relationship")
u1_values = list(map(int,input('enter the values of u1: ').split()))
u1 = np.array(u1_values)
u2_values = list(map(int,input('enter the values of u2: ').split()))
u2 = np.array(u2_values)
rel_finder(u1,u2)

# # 8. frequency distribution:
# import numpy as np
# def freq_dist(hell):
#     summation = 0
#     hell = list(hell)
#     n = len(hell)
#     for i in range(18,n):
#         frequency = hell.count(i)
#         print(f"frequency of {[i]}th element is {frequency}")
#         summation+=hell[i]
#         amean = summation/n
#         variance = frequency* (hell[i]-amean)**2
#         print(f"variance of the {[i]}th value is {variance}")
# hell = np.array([18,21,23,27,27,30,32,32,32,36,37,41,42,42,43,48,48,51,55,58,60,62,63,67,68,88])
# freq_dist(hell)

# import numpy as np
# import math as m
# def freq_dist_and_moments_print(data):
#     data = list(data)
#     mean = sum(data) / len(data)
#     total_freq = len(data)

#     moment2 = 0
#     moment3 = 0
#     moment4 = 0
#     sum_fixi = 0
#     sum_fi = 0

#     print(f"Mean: {mean:.2f}")
#     print(" Creatinine  |  fi  | fixi | (x-mean)^2 | (x-mean)^3 | (x-mean)^4 |")
#     print("---------------------------------------------------------------")

#     for i in sorted(set(data)):
#         fi = data.count(i)
#         fixi = fi * i
#         dev = i - mean

#         moment2 += fi * dev**2
#         moment3 += fi * dev**3
#         moment4 += fi * dev**4
#         sum_fixi += fixi
#         sum_fi += fi

#         print(f"{i:5.2f} | {fi:4} | {fixi:8} | {dev**2:11.8f} | {dev**3:11.8f} | {dev**4:11.8f} |")

#     variance = moment2 / total_freq
#     third_moment = moment3 / total_freq
#     fourth_moment = moment4 / total_freq
#     beta_1 = (third_moment)**2/(variance)**3
#     gamma_1 = m.sqrt(beta_1)
#     beta_2 = fourth_moment/(variance)**2

#     print("----------------------------------------------------------------")
#     print(f"Total | n={sum_fi:4} | {sum_fixi:4.8f} | {moment2:11.8f} | {moment3:11.8f} | {moment4:11.8f} |")
#     print(f"\nVariance (2nd moment)  :{variance:.8f}")
#     print(f"3rd Central Moment     :{third_moment:.8f}")
#     print(f"4th Central Moment     :{fourth_moment:.8f}")
#     print(f"value of ß1 is:        :{beta_1:.8f}")
#     print(f"value of Γ1 is:        :{gamma_1:.8f}")
#     print(f"value of ß2 is:        :{beta_2:.8f}")

#     if gamma_1>0:
#         print("The distribution is positively skewed.")
#     elif gamma_1<0:
#         print("The distribution is negatively skewed.")
#     else:
#         print("Inconclusive.")
#     if beta_2>3:
#         print("The distribution is leptokurtic.")
#     elif beta_2<3:
#         print("The distribution is platykurtic")
#     else:
#         print("The distribution is mesokurtic.")

# hell = np.array([])
# freq_dist_and_moments_print(hell)

# 9. regression equation: least square method
import matplotlib.pyplot as plt
def regression(tt,tcp):
    n = len(tt)
    sum_of_x = 0
    sum_of_x2 = 0
    sum_of_y = 0
    product_of_xandy = 0
    for i in range(n):
        sum_of_x+=tt[i]
        sum_of_x2+=tt[i]**2
    print(f"sum of x is:{sum_of_x}\nsum of x**2 is:{sum_of_x2}")
    for i in range(n):
        sum_of_y+=tcp[i]
    print(f"sum of y is:{sum_of_y:.2f}")
    for i in range(n):
        product_of_xandy += (tt[i]*tcp[i])
    print(f"the sum product of x and y is: {product_of_xandy:.2f}")
    b = (product_of_xandy-((sum_of_x*sum_of_y)/n))/(sum_of_x2-(sum_of_x**2)/n)
    a = (sum_of_y/n)-b*(sum_of_x/n)
    print(f'the estimated least square line is\ny={a:.2f}+{b:.2f}x')
tt_val = list(map(int,input("enter the values of tt: ").split()))
tt = np.array(tt_val)
tcp_val = list(map(int,input("enter the values of tcp: ").split()))
tcp = np.array(tt_val)
regression(tt,tcp)
plt.style.use('dark_background')
plt.plot(tt,tcp,'ro',markersize = 15)
plt.xlabel('Training time')
plt.ylabel('Time to complete the project')
plt.grid(True)
plt.show()        

# 10. distribution plotting:
import seaborn as sbn
plt.style.use("dark_background")
sbn.histplot(tt,kde=True,stat="density",bins=20)
"""kde=True: ekta smooth curve diye distribution dekhay.
bins: curve smooth kore adjust kore ."""
plt.xlabel("value")
plt.ylabel("density")
plt.show()

""" 11. a python program which takes a finite sequence of n terms as its input 
and return the type of sequence as its output."""
def series_identifier(s):
    n = len(s)
    d = 0
    r = 1
    for i in range(0,n-1):
        d = s[i+1]-s[i]
        r = s[i+1]/[i]
    for i in range(0,n-1):
        if s[i+1]-s[i] == d:
           return True
        elif s[i+1]/[i] == r:
            return True
        else:
            print("Error.")
    print
s = np.array([2,4,6,8,10])
series_identifier(s)

#data analysis: football team
lineup = {'player1':{'name':'Kylian Mbappe','kit number':9,'position':'forward','stats':{'goals':33,'assists':5,'appearences':35}},
          'player2':{'name':'Vinicius Jr','kit number':7,'position':'forward','stats':{'goals':19,'assists':10,'appearences':35}},
          'player3':{'name':'Jude Bellingham','kit number':5,'position':'midfielder','stats':{'goals':12,'assists':11,'appearences':35}}
          }
print(list(lineup.keys()))
print(lineup['player1'])
print(lineup['player2'])
print(lineup['player3'])
lineup['player1'].update({'kit number':10})
goals_mbappe = lineup['player1']['stats']['goals']
assists_mbappe = lineup['player1']['stats']['assists']
appearences_mbappe = lineup['player1']['stats']['appearences']
goals_per_matches_mbappe = goals_mbappe/appearences_mbappe
assists_per_matches_mbappe = assists_mbappe/appearences_mbappe
goals_vini = lineup['player2']['stats']['goals']
assits_vini = lineup['player2']['stats']['assists']
appearences_vini = lineup['player2']['stats']['appearences']
goals_per_matches_vini = goals_vini/appearences_vini
assists_per_matches_vini = assits_vini/appearences_vini
goals_bellinhgam = lineup['player3']['stats']['goals']
assists_bellingham = lineup['player3']['stats']['assists']
appearences_bellingham = lineup['player3']['stats']['appearences']
assists_per_matches_bellingham = assists_bellingham/appearences_bellingham
print(f"{goals_per_matches_mbappe:.2f}")
print(f"{goals_per_matches_vini:.2f}")
if goals_per_matches_mbappe>goals_per_matches_vini:
    print("Kylian Mbappe wins the golden boot.")
else:
    print("Vinicius Jr wins the golden boot.")
if assists_per_matches_mbappe>assists_per_matches_vini:
    print(f"Kylian also wins the playmaker of the year award.")
elif assists_per_matches_vini>assists_per_matches_bellingham:
    print(f"Vinicius Jr wins the playmaker of the year award with {assits_vini} assists.")
else:
    print(f"Jude Bellingham wins the playmaker of the year award with {assists_bellingham} assists.")