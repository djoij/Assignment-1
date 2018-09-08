import pandas as pd
import numpy as np

all_regions,year_string=[],[]
all_regions.append('south')
all_regions.append('east')
all_regions.append('west')
all_regions.append('north')
all_regions.append('ne')
all_regions.append('central')
year_string.append('2012-13')
year_string.append('2013-14')
year_string.append('2014-15')
combine=[]
for y in year_string:
	for ar in all_regions:
		combine.append(y + ' ' + ar)
#print(combine)

a = pd.read_csv('drop-out-rate.csv')
regions= pd.read_csv('regions.csv')
a.rename(columns={'State_UT': 'States'}, inplace=True)
# madhya pradesh, arunachal pradesh,  tamil nadu
a=a.replace('Dadra & Nagar Haveli','D & N Haveli')
a=a.replace('Delhi','NCT of Delhi')
a=pd.merge(a,regions,on='States', how='outer')
a=a.replace('NR',np.nan).apply(pd.to_numeric, errors='ignore')
a["reference"] = a["year"].map(str) + ' ' + a["Region"]
for i in combine:
	a.loc[a['reference']==i]=a.loc[a['reference']==i].fillna(a.loc[a['reference']==i].mean().round(2))
#a.fillna(value.groupby("States").get_group('All_India GDP').mean(), inplace=True)
a.to_csv('ifnan.csv')
#b=a.loc[a['year']=='2012-13']
#a.loc[a['year']=='2012-13']=a.loc[a['year']=='2012-13'].fillna(a.loc[a['year']=='2012-13'].mean().round(2))
#a.loc[a['year']=='2012-13'].loc[a['Region']=='ne']=a.loc[a['year']=='2012-13'].loc[a['Region']=='ne'].fillna(a.loc[a['year']=='2012-13'].loc[a['Region']=='ne'].mean().round(2))
#b=a.groupby('year').get_group('2012-13').groupby('Region').get_group('ne')
#print(a.groupby('year' , as_index=False).get_group('2012-13').groupby('Region' , as_index=False).get_group('ne').fillna(b.mean()))
'''for ar in all_regions:
	for y in year_string:
		b=a.loc[a['year']==y]
		a.loc[a['year']==y].loc[a['Region']==ar]=a.loc[a['year']==y].loc[a['Region']==ar].fillna(b.loc[a['Region']==ar].mean().round(2))
		#a.groupby('year').get_group(y).groupby('Region').get_group(ar).fillna(a.groupby('year').get_group(y).groupby('Region').get_group(ar).mean().round(2), inplace=True) # works like a charm
a.to_csv('ifnan.csv')'''
#print(a.loc[a['year']=='2014-15'].groupby('Region').get_group('south').fillna(a.loc[a['year']=='2014-15'].groupby('Region').get_group('south').mean().round(2)))
#a.loc[a['year']=='2014-15']=a.loc[a['year']=='2014-15'].fillna(a.loc[a['year']=='2014-15'].mean().round(2),inplace=True)
#a.groupby('year', as_index=False).get_group('2014-15').groupby('Region', as_index=False).get_group('south').fillna(a.groupby('year', as_index=False).get_group('2014-15').groupby('Region', as_index=False).get_group('south').mean().round(2),inplace=True)
print(a.groupby('year').get_group('2012-13').groupby('Region').get_group('central'))
