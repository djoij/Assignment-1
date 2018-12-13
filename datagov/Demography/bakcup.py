import pandas as pd
import numpy as np
#loading files

child_sex_ratio = pd.read_csv('child-sex-ratio-0-6-years.csv')
child_sex_ratio.rename(columns={'Country/ States/ Union Territories Name': 'States'}, inplace=True)
#df[Missing Region] = np.nan
sex_ratio = pd.read_csv('sex-ratio.csv')
growth_rate = pd.read_csv('decadal-growth-rate.csv')
regions= pd.read_csv('regions.csv')

#change to unified state for heading

child_sex_ratio=pd.merge(child_sex_ratio,regions,on='States', how='outer')
#child_sex_ratio.fillna("NaN").to_csv('check.csv')

missing_region=child_sex_ratio[child_sex_ratio['Category'].isnull()]['Region'] #finding missing region
for i in missing_region:
	ch=i
child_sex_ratio.fillna(child_sex_ratio.groupby("Region").get_group(ch).transform("mean"), inplace=True)
child_sex_ratio.rename(columns={'States' : 'Country/ States/ Union Territories Name'}, inplace=True)
child_sex_ratio.fillna('State').drop('Region', axis=1).to_csv('check.csv')

