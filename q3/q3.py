import pandas as pd
import numpy as np

f_d = pd.read_csv('Final_Merge.csv')
f_d=f_d.fillna(0)
f_d=f_d.set_index('Country/State/UT_Name').reset_index()
f_d.drop('Unnamed: 0', axis=1, inplace=True)

f_d.corr().to_csv('corr.csv')