import pandas as pd
import numpy as np
from sklearn import preprocessing
from operator import itemgetter, attrgetter
f_d = pd.read_csv('Final_Merge.csv')

f_d=f_d.fillna(0)
b=[]
for i in range(37):
	a=[]
	for j in range(2,360):
		a.append(f_d.iloc[i][j])
	b.append(a)
#print(len(b))
b_normalized = preprocessing.normalize(b, norm='l2')
vec=[]
for i in range(1,37):
	sum=0
	for j in range(356):
		sum=sum+b_normalized[0][j]*b_normalized[i][j]
	vec.append(sum)


s=[]
for idx,i in enumerate(vec):
	s.append((i,idx))
s=sorted(s, key=itemgetter(0),reverse=True)
ind=[]
for i in range(5):
	(a,b)=s[i]
	ind.append(b+1)
#print(ind)
for i in range(len(ind)):
	n=ind[i]
	print(f_d.iloc[n][1])
#print(b_normalized[35][357])
#f_d.drop('Country/State/UT_Name', axis=1, inplace=True)
