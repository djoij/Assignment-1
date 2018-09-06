import pandas as pd
import numpy as np

gdp = pd.read_csv('gross-domestic-product-gdp-constant-price.csv')

region=pd.read_csv('regions.csv')
#replace ( space with no space)
# make unified states value for all
gdp["Items Description"] = gdp["Items Description"].map(str) + ' ' + gdp["Duration"]

#gdp.drop('Items Description', axis=1, inplace=True)
gdp.drop('Duration', axis=1, inplace=True)
gdp.rename(columns={'Items Description': 'States'}, inplace=True)
gdp=gdp.fillna("NaN").replace(0,"NaN")
gdp=gdp.set_index('States').T.reset_index()
gdp.rename(columns={'index': 'States'}, inplace=True)
gdp.to_csv('null.csv')
#gdp=gdp.set_index('States').T
#.groupby('States').first()	
#print(gdp.groupby('Items Description and Duration').first())
gdp=pd.merge(gdp,region,on='States', how='outer')
gdp.to_csv('null.csv')
#Regions and Item Wise group then get group by year uska mean fill na?