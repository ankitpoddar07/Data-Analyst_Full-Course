# mehods --- head()  &  tail()
# head() 5
# tail(n) 5

import pandas as pd
df = pd.read_csv("sales_data_sample.csv" , encoding="latin1")
# Display the first 5 rows of the DataFrame
print('Display 5 rows of first')
print(df.head(5))
# Display the last 5 rows of the DataFrame
print('Display 5 rows of last')
print(df.tail(5))