import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv('demography_two_columns.csv')
plt.scatter(data['Decadal growth rate - Rural - 1991-01'], data['Child sex ratio in population (0-6 age group) - Total - 2011'])
plt.xlabel('Decadal growth rate - Rural - 1991-01')
plt.ylabel('Child sex ratio in population (0-6 age group) - Total - 2011')
plt.title('Demography_Scatter')
plt.show()