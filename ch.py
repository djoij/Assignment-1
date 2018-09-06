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

'''for idx,j in enumerate(a):
	j.rename(columns={'Country/ States/ Union Territories Name': 'States'}, inplace=True)
	j=pd.merge(j,regions,on='States', how='outer')

	missing_region=j[j['Category'].isnull()]['Region']
	for i in missing_region:
		j.fillna(j.groupby("Region").get_group(i).transform("mean").round(2), inplace=True)
		j.rename(columns={'States' : 'Country/ States/ Union Territories Name'}, inplace=True)
		j.fillna('State').drop('Region', axis=1).to_csv(b[idx])'''

