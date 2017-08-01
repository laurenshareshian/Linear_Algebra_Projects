#this program cracks the weightings assigned for the 2013 US News World & Report
# US Liberal Arts Colleges by doing a least squares projection
import numpy as np
from scipy import linalg

college_file = np.genfromtxt('collegedata.csv',delimiter=',', skip_header=1, dtype=None)
college_variables = np.genfromtxt('collegedata.csv',delimiter=',', skip_footer=25,dtype=None)

coefficients=np.zeros((len(college_file),14))
rankings=np.zeros(len(college_file))

for i in range(len(college_file)):
    rankings[i]=college_file[i][1] # list of rankings

for j in range(14):
    for i in range(len(college_file)):
        coefficients[i][j]=college_file[i][j+2] #matrix of college data

weights=linalg.inv(coefficients.T.dot(coefficients)).dot(coefficients.T).dot(rankings)

weight_dict={}
for i in range(len(weights)):
    weight_dict[college_variables[i+2]]=weights[i]

lst = list()
for key, val in weight_dict.items():
    lst.append( (val, key) )
    lst.sort(reverse=True)

print('the largest positive weights are most positively influential')
print('the largest negative weights are most negatively influential')
for item in lst:
    print(item)