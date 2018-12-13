import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv('economy_two_columns.csv')
plt.scatter(data['GSDP - CONSTANT PRICES (` in Crore)_2015-16 (gdp_constant)'], data['GSDP - CONSTANT PRICES (` in Crore)_2012-13 (gdp_constant)'])
plt.xlabel('GSDP - CONSTANT PRICES (` in Crore)_2015-16 (gdp_constant)')
plt.ylabel('GSDP - CONSTANT PRICES (` in Crore)_2012-13 (gdp_constant)')
plt.title('Economy_Scatter')
plt.show()