import pandas as pd
import numpy as np

gdp = pd.read_csv('gross-domestic-product-gdp-constant-price.csv')
region=pd.read_csv('regions.csv')
#replace ( space with no space)
# make unified states value for all
gdp["Items Description"] = gdp["Items Description"].map(str) + ' ' + gdp["Duration"]

#gdp.drop('Items Description', axis=1, inplace=True)
gdp.rename(columns={'Andaman & Nicobar Islands': 'A & N Islands', 'Delhi':'NCT of Delhi'}, inplace=True)
gdp.drop('Duration', axis=1, inplace=True)
gdp.rename(columns={'Items Description': 'States'}, inplace=True)
#gdp=gdp.fillna("NaN").replace(0,"NaN")
gdp=gdp.set_index('States').T.reset_index()
gdp.rename(columns={'index': 'States'}, inplace=True)
#gdp=gdp.set_index('States').T
#.groupby('States').first()	
#print(gdp.groupby('Items Description and Duration').first())
gdp=pd.merge(gdp,region,on='States', how='outer')
#gdp=gdp.fillna("NaN").replace(0,"NaN")
#gdp=gdp.fillna("NaN").replace("NaN",' ')
#print(gdp.isnull())
#gdp.isnull().to_csv('null.csv')
#find missing 0 ko nahi consider karra
#gdp=gdp.groupby("Region") # giving mean check with or without missing
#do something about the 0
gdp.loc[gdp['Region']=="south"]=gdp.loc[gdp['Region']=="south"].fillna(gdp.loc[gdp['Region']=="south"].mean().round(2)) #works like a charm
#gdp.groupby('Region').get_group('south').fillna(gdp.groupby('Region').get_group('south').mean().round(2), inplace=True)
#print(gdp.groupby('Region').get_group('south'))
gdp.to_csv('null.csv')
#Regions and Item Wise group then get group by year uska mean fill na?