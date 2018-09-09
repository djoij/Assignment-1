import pandas as pd
import numpy as np

all_regions=[]
all_regions.append('south')
all_regions.append('east')
all_regions.append('west')
all_regions.append('north')
all_regions.append('ne')
all_regions.append('central')

regions= pd.read_csv('regions.csv')


drop_rate_year=[]
drop_rate_year.append('2012-13')
drop_rate_year.append('2013-14')
drop_rate_year.append('2014-15')
combine_drop_rate=[]
for y in drop_rate_year:
	for ar in all_regions:
		combine_drop_rate.append(y + ' ' + ar)
drop_rate = pd.read_csv('drop-out-rate.csv')
drop_rate.rename(columns={'State_UT': 'States'}, inplace=True)
# madhya pradesh, arunachal pradesh,  tamil nadu
drop_rate=drop_rate.replace('Dadra & Nagar Haveli','D & N Haveli')
drop_rate=drop_rate.replace('Delhi','NCT of Delhi')
drop_rate=pd.merge(drop_rate,regions,on='States', how='outer')
drop_rate=drop_rate.replace('NR',np.nan).apply(pd.to_numeric, errors='ignore')
drop_rate["reference"] = drop_rate["year"].map(str) + ' ' + drop_rate["Region"]
for i in combine_drop_rate:
	drop_rate.loc[drop_rate['reference']==i]=drop_rate.loc[drop_rate['reference']==i].fillna(drop_rate.loc[drop_rate['reference']==i].mean().round(2))
drop_rate.drop('reference', axis=1, inplace=True)
drop_rate.loc[drop_rate['Region']=='central']=drop_rate.loc[drop_rate['Region']=='central'].fillna(drop_rate.loc[drop_rate['year']=='2012-13'].mean().round(2))
drop_rate.loc[drop_rate['year']=='2012-13']=drop_rate.loc[drop_rate['year']=='2012-13'].fillna(drop_rate.loc[drop_rate['year']=='2012-13'].mean().round(2))
drop_rate.loc[drop_rate['year']=='2014-15']=drop_rate.loc[drop_rate['year']=='2014-15'].fillna(drop_rate.loc[drop_rate['year']=='2014-15'].mean().round(2))

q=[]
for i in drop_rate_year:
	q.append(drop_rate.loc[drop_rate['year']==i])
	
for val in range(len(drop_rate_year)) :
	q[val].drop('year', axis=1, inplace=True)
	q[val].drop('Region', axis=1, inplace=True)
	for i in q[val].columns.values:
		if(i != 'States' ):
			name='drop_out_rate' + '_' + i + '_' + drop_rate_year[val]
			q[val].rename(columns={i:name}, inplace=True)

drop_rate=q[0]
for i in range(1,len(drop_rate_year)):
	drop_rate=pd.merge(drop_rate,q[i],on='States', how='outer')
#drop_rate.to_csv('check.csv')



hi_ed=pd.read_csv('gross-enrolment-ratio-higher-education.csv')
combine_higher_education,higher_education_year=[],[]
higher_education_year.append('2010-11')
higher_education_year.append('2011-12')
higher_education_year.append('2012-13')
higher_education_year.append('2013-14')
higher_education_year.append('2014-15')
higher_education_year.append('2015-16')
for y in higher_education_year:
	for ar in all_regions:
		combine_higher_education.append(y + ' ' + ar)
hi_ed.rename(columns={'Country/ State/ UT Name': 'States', 'Year':'year'}, inplace=True)
hi_ed=hi_ed.replace('Dadra & Nagar Haveli','D & N Haveli')
hi_ed=hi_ed.replace('Delhi','NCT of Delhi')
hi_ed=hi_ed.replace('Andaman & Nicobar Islands','A & N Islands')
hi_ed=hi_ed.replace('Chhatisgarh','Chhattisgarh')
hi_ed=hi_ed.replace('Uttrakhand','Uttarakhand')
hi_ed=hi_ed.replace('Jammu and Kashmir','Jammu & Kashmir')
hi_ed=pd.merge(hi_ed,regions,on='States', how='outer') #hi_ed=hi_ed.replace(0,np.nan)
hi_ed=hi_ed.replace(0,np.nan)
hi_ed=hi_ed.replace('NA',np.nan).apply(pd.to_numeric, errors='ignore')
hi_ed["reference"] = hi_ed["year"].map(str) + ' ' + hi_ed["Region"]
for i in combine_higher_education:
	hi_ed.loc[hi_ed['reference']==i]=hi_ed.loc[hi_ed['reference']==i].fillna(hi_ed.loc[hi_ed['reference']==i].mean().round(2))
hi_ed.drop('reference', axis=1, inplace=True)
#hi_ed.to_csv('ifnan.csv')
q=[]
for i in higher_education_year:
	q.append(hi_ed.loc[hi_ed['year']==i])
	
for val in range(len(higher_education_year)) :
	q[val].drop('year', axis=1, inplace=True)
	q[val].drop('Region', axis=1, inplace=True)

	for i in q[val].columns.values:
		if(i != 'States' ):
			name='higher_education' + '_' + i + '_' + higher_education_year[val]
			q[val].rename(columns={i:name}, inplace=True)
	#print(q[val])
hi_ed=q[0]
for i in range(1,len(higher_education_year)):
	hi_ed=pd.merge(hi_ed,q[i],on='States', how='outer')
#hi_ed.to_csv('merge.csv')
#hi_ed.to_csv('gross-enrolment-ratio-higher-education.csv')


rest_data=[]
rest_data.append(pd.read_csv('gross-enrolment-ratio-schools.csv'))
rest_data.append(pd.read_csv('percentage-schools-computers.csv'))
rest_data.append(pd.read_csv('percentage-schools-drinking-water.csv'))
rest_data.append(pd.read_csv('percentage-schools-electricity.csv'))
rest_data.append(pd.read_csv('percentage-schools-girls-toilet.csv'))
rest_data.append(pd.read_csv('percentage-schools-boys-toilet.csv'))
year,combine=[],[]
year.append('2013-14')
year.append('2014-15')
year.append('2015-16')
for y in year:
	for ar in all_regions:
		combine.append(y + ' ' + ar)
name1=[]
name1.append('enrolment_ratio')
name1.append('computers')
name1.append('drinking_water')
name1.append('electricity')
name1.append('girls_toilet')
name1.append('boys_toilet')
for idx,test in enumerate(rest_data):
	test.rename(columns={'State_UT': 'States', 'Year':'year'}, inplace=True)
	test=test.replace('Dadra & Nagar Haveli','D & N Haveli')
	test=test.replace('Delhi','NCT of Delhi')
	test=test.replace('Andaman & Nicobar Islands','A & N Islands')
	#test=test.replace('Chhatisgarh','Chhattisgarh')
	test=test.replace('Uttaranchal','Uttarakhand')
	test=test.replace('Jammu and Kashmir','Jammu & Kashmir')
	test=test.replace('Jammu And Kashmir','Jammu & Kashmir')
	test=test.replace('Pondicherry','Puducherry')
	test=test.replace('MADHYA PRADESH','Madhya Pradesh')
	test=pd.merge(test,regions,on='States', how='outer')
	test["reference"] = test["year"].map(str) + ' ' + test["Region"]
	test=test.replace('@',np.nan)
	test=test.replace(0,np.nan)
	test=test.replace('NR',np.nan).apply(pd.to_numeric, errors='ignore')
	for i in combine:
		test.loc[test['reference']==i]=test.loc[test['reference']==i].fillna(test.loc[test['reference']==i].mean().round(2))
	test.drop('reference', axis=1, inplace=True)
	q=[]
	for i in year:
		q.append(test.loc[test['year']==i])
		
	for val in range(len(year)) :
		q[val].drop('year', axis=1, inplace=True)
		q[val].drop('Region', axis=1, inplace=True)

		for i in q[val].columns.values:
			if(i != 'States' ):
				name=name1[idx] + '_' + i + '_' + year[val]
				q[val].rename(columns={i:name}, inplace=True)
		#print(q[val])
	test=q[0]
	for i in range(1,len(year)):
		test=pd.merge(test,q[i],on='States', how='outer')
	#test.to_csv('ifnan.csv')
	rest_data[idx]=test

mergedata3=rest_data[0]
for i in range(1,(len(rest_data))):
	mergedata3=pd.merge(mergedata3,rest_data[i],on='States', how='outer')


mergedata=pd.merge(drop_rate,hi_ed,on='States', how='outer')
mergedata=pd.merge(mergedata,mergedata3,on='States', how='outer')

mergedata.to_csv('mergedata.csv')


