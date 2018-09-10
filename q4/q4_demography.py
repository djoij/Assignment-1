import pandas as pd
import numpy as np
import random

f_d = pd.read_csv('demography_merge.csv')
f_d=f_d.set_index('States').reset_index()
f_d=f_d.fillna(f_d.mean().round(2))
region=pd.read_csv('regions.csv')
f_d.drop('Unnamed: 0', axis=1, inplace=True)
f_d=pd.merge(f_d,region,on='States', how='outer')
b=[]
for i in range(1,37):
	a=[]
	for j in range(1,19):
		a.append(f_d.iloc[i][j])
	b.append(a)
b=np.asarray(b)
b=b/(np.linalg.norm(b, axis=0))
s=np.zeros((18))

def euclidian(r_int):
	mini=100
	for i in same_class:
		if( i!= r_int+1):
			df=b[r_int]-b[i-1]
			df=np.linalg.norm(df, axis=0)
			#print(df)
			if(df<mini):
				mina=i-1
				mini = df
	mini=100
	for i in range(1,37):
		if(i not in same_class):
			df=b[r_int]-b[i-1]
			df=np.linalg.norm(df, axis=0)
			if(df<mini):
				minb=i-1
				mini = df

	return [mina,minb]

for i in range(1):
	r_int=random.randint(0,35)
	reg=f_d.iloc[r_int+1][19]
	same_class=np.where(f_d["Region"] == reg)
	same_class=np.asarray(same_class)
	same_class=same_class[0]	
	[mina,minb]=euclidian(r_int)
	nearest_hit=(b[mina]-b[r_int]) ** 2
	nearest_miss=(b[minb]-b[r_int]) ** 2
	s=s+nearest_hit	- nearest_miss
maximum=-100	

for i in range(len(s)):
	if(s[i]>maximum):
		max_index=i
		maximum=s[i]
sec_max=-100
for i in range(len(s)):
	if(s[i]!=maximum and s[i]>sec_max):
		sec_max_index=1
		sec_max=s[i]
first_attribute=f_d.columns[max_index+1]
second_attribute=f_d.columns[sec_max_index+1]
print(first_attribute)
print(second_attribute)

imp_data = f_d.ix[:, ['States', first_attribute , second_attribute]]
imp_data.rename(columns={'States':'Country/State/UT_Name'},inplace=True)
imp_data.to_csv('demography_two_columns.csv')