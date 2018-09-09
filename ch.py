import pandas as pd
import numpy as np
#loading files
a,b=[],[]
b.append('child-sex-ratio-0-6-years.csv')
b.append('sex-ratio.csv')
b.append('decadal-growth-rate.csv')
a.append(pd.read_csv('child-sex-ratio-0-6-years.csv'))
a.append(pd.read_csv('sex-ratio.csv'))
a.append(pd.read_csv('decadal-growth-rate.csv'))
regions= pd.read_csv('regions.csv')

for idx,j in enumerate(a):
	j.rename(columns={'Country/ States/ Union Territories Name': 'States'}, inplace=True)
	j=pd.merge(j,regions,on='States', how='outer')

	missing_region=j[j['Category'].isnull()]['Region']
	for i in missing_region:
		j.fillna(j.groupby("Region").get_group(i).transform("mean").round(2), inplace=True)
		#j.rename(columns={'States' : 'Country/ States/ Union Territories Name'}, inplace=True)
		j=j.drop('Region', axis=1)
		j=j.drop('Category',axis=1)
		#j.to_csv('check.csv')
		a[idx]=j


mergedata1=a[0]
for i in range(1,(len(a))):
	mergedata1=pd.merge(mergedata1,a[i],on='States', how='outer')
mergedata1.to_csv('demography_merge.csv')

