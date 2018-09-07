import pandas as pd
import numpy as np
#store all region
all_regions=[]
all_regions.append('south')
all_regions.append('east')
all_regions.append('west')
all_regions.append('north')
all_regions.append('ne')
all_regions.append('central')

#input
gdp = pd.read_csv('gross-domestic-product-gdp-constant-price.csv')
gdp=gdp.drop(gdp.index[11]) #drop row with all 0
region=pd.read_csv('regions.csv')
#new column by combining 2
gdp["Items Description"] = gdp["Items Description"].map(str) + ' ' + gdp["Duration"]
gdp.rename(columns={'Andaman & Nicobar Islands': 'A & N Islands', 'Delhi':'NCT of Delhi'}, inplace=True) #making same as region data
gdp.drop('Duration', axis=1, inplace=True) #after merge to column drop 1 column
gdp.rename(columns={'Items Description': 'States'}, inplace=True) # change index to states
#gdp=gdp.fillna("NaN").replace(0,"NaN")
gdp=gdp.set_index('States').T.reset_index() #reset index so that indexing on removes
gdp.rename(columns={'index': 'States'}, inplace=True) #indexing resets creates index header change it to states
gdp=pd.merge(gdp,region,on='States', how='outer') #merge region and working one
for i in all_regions:
	gdp.loc[gdp['Region']==i]=gdp.loc[gdp['Region']==i].fillna(gdp.loc[gdp['Region']==i].mean().round(2))  #works like a charm
gdp.fillna(gdp.groupby("States").get_group('All_India GDP'), inplace=True) #need divide by states
gdp.to_csv('null.csv')