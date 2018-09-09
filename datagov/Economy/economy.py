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

economy,name=[],[]
name.append('gross-domestic-product-gdp-constant-price.csv')
name.append('gross-domestic-product-gdp-current-price.csv')
name.append('state-wise-net-domestic-product-ndp-constant-price.csv')
name.append('state-wise-net-domestic-product-ndp-current-price.csv')
economy.append(pd.read_csv('gross-domestic-product-gdp-constant-price.csv'))
economy.append(pd.read_csv('gross-domestic-product-gdp-current-price.csv'))
economy.append(pd.read_csv('state-wise-net-domestic-product-ndp-constant-price.csv'))
economy.append(pd.read_csv('state-wise-net-domestic-product-ndp-current-price.csv'))
#input
region=pd.read_csv('regions.csv')
for idx, value in enumerate(economy):
	if(value.index[-1]==11):
		value=value.drop(value.index[11]) #drop row with all 0
	#new column by combining 2
	value["Items Description"] = value["Items Description"].map(str) + ' ' + value["Duration"]
	#Items  Desc, Item Desc
	value.rename(columns={'Andaman & Nicobar Islands': 'A & N Islands', 'Delhi':'NCT of Delhi','West Bengal1':'West Bengal'}, inplace=True) #making same as region data
	value.drop('Duration', axis=1, inplace=True) #after merge to column drop 1 column
	value.rename(columns={'Items Description': 'States'}, inplace=True) # change index to states
	#value=value.fillna("NaN").replace(0,"NaN")
	value=value.set_index('States').T.reset_index() #reset index so that indexing on removes / could have used (groupby States as_index=False)
	value.rename(columns={'index': 'States'}, inplace=True) #indexing resets creates index header change it to states
	value=pd.merge(value,region,on='States', how='outer') #merge region and working one
	for i in all_regions:
		value.loc[value['Region']==i]=value.loc[value['Region']==i].fillna(value.loc[value['Region']==i].mean().round(2))  #works like a charm
	if(idx==1 or idx ==0):
		value.fillna(value.groupby("States").get_group('All_India GDP').mean(), inplace=True) #need to divide by no. states
		#print("GDP")
	else:
		value.fillna(value.groupby("States").get_group('All_India NDP').mean(), inplace=True) #need to divide by no. states
		#print("NDP")
	#value.to_csv(name[idx])
	value.to_csv('null.csv')
