import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv('education_two_columns.csv')
plt.scatter(data['drop_out_rate_Upper Primary_Girls_2013-14'], data['drop_out_rate_Primary_Girls_2012-13'])
plt.xlabel('drop_out_rate_Upper Primary_Girls_2013-14')
plt.ylabel('drop_out_rate_Primary_Girls_2012-13')
plt.title('Education_Scatter')
plt.show()