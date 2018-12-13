import pandas as pd
import numpy as np
#loading files

child_sex_ratio = pd.read_csv('literacy-rate-7-years.csv')
child_sex_ratio.rename(columns={'Country/ States/ Union Territories Name': 'States'}, inplace=True)
regions= pd.read_csv('regions.csv')

#change to unified state for heading

child_sex_ratio=pd.merge(child_sex_ratio,regions,on='States', how='outer')

missing_region=child_sex_ratio[child_sex_ratio['Category'].isnull()]['Region'] #finding missing region
for i in missing_region:
	ch=i
child_sex_ratio.fillna(child_sex_ratio.groupby("Region").get_group(ch).transform("mean").round(2), inplace=True)
child_sex_ratio.rename(columns={'States' : 'Country/ States/ Union Territories Name'}, inplace=True)
child_sex_ratio.fillna('State').drop('Region', axis=1).to_csv('check.csv')

