import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.neighbors import NearestNeighbors
from operator import itemgetter, attrgetter
import math

f_d = pd.read_csv('Final_Merge.csv')
f_d=f_d.fillna(0)
b=[]
for i in range(37):
	a=[]
	for j in range(2,361):
		a.append(f_d.iloc[i][j])
	b.append(a)
l=len(b)
print(b[l-1])
vec=[]
for i in range(1,37):
	sum=0
	for j in range(357):
		sum=sum+(b[0][j]-b[i][j]) ** 2	
	vec.append(math.sqrt(sum))
s=[]
for idx,i in enumerate(vec):
	s.append((i,idx))
s=sorted(s, key=itemgetter(0))
ind=[]
for i in range(5):
	(a,b)=s[i]
	ind.append(b+1)
#print(ind)
for i in range(len(ind)):
	n=ind[i]
	print(f_d.iloc[n][1])
'''#

    """
    A simple euclidean distance function
    """
    inner_value = 0
    for k in distance_columns:
        inner_value += (row[k] - selected_player[k]) ** 2
    return math.sqrt(inner_value)

# Find the distance from each player in the dataset to lebron.
lebron_distance = f_d.apply(euclidean_distance, axis=1)'''