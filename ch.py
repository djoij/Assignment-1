import pandas as pd

#loading files

child_sex_ratio = pd.read_csv('child-sex-ratio-0-6-years.csv')
sex_ratio = pd.read_csv('sex-ratio.csv')
growth_rate = pd.read_csv('decadal-growth-rate.csv')
regions= pd.read_csv('regions.csv')
#change to unified state for heading
child_sex_ratio=pd.merge(child_sex_ratio,regions,on='States', how='outer')
child_sex_ratio = child_sex_ratio.fillna("NaN")
child_sex_ratio.groupby('Region').sum().to_csv('check.csv') #sum pura nahi ara
#child_sex_ratio=child_sex_ratio.sort_values(by=['Region'])
#child_sex_ratio.to_csv('check.csv')
# NaN wala region wise sum them impute
