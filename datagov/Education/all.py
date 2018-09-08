import pandas as pd
import numpy as np

a = pd.read_csv('drop-out-rate.csv')
regions= pd.read_csv('regions.csv')
a.rename(columns={'State_UT': 'States'}, inplace=True)
# madhya pradesh, arunachal pradesh,  tamil nadu
a=a.replace('Dadra & Nagar Haveli','D & N Haveli')
a=a.replace('Delhi','NCT of Delhi')
a=pd.merge(a,regions,on='States', how='outer')
a=a.replace('NR','NaN')
b=a.loc[a['year']=='2012-13']
a.loc[a['year']=='2012-13']=a.loc[a['year']=='2012-13'].fillna(a.loc[a['year']=='2012-13'].mean().round(2))
#a.loc[a['year']=='2012-13'].loc[a['Region']=='ne']=a.loc[a['year']=='2012-13'].loc[a['Region']=='ne'].fillna(a.loc[a['year']=='2012-13'].loc[a['Region']=='ne'].mean().round(2))
#b=a.groupby('year').get_group('2012-13').groupby('Region').get_group('ne')
#print(a.groupby('year').get_group('2012-13').groupby('Region').get_group('ne').fillna(b.mean()))
print(a.groupby('Region').get_group('ne').mean())