import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv('two_columns.csv')
plt.scatter(data['Decadal growth rate - Urban - 1991-01'], data['Child sex ratio in population (0-6 age group) - Total - 2011'])
plt.xlabel('Decadal growth rate - Urban - 1991-01')
plt.ylabel('Child sex ratio in population (0-6 age group) - Total - 2011')
plt.title('All_Merge_Scatter')
plt.show()