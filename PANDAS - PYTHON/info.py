# Importing the pandas library

import pandas as pd

# df = pd.read_csv("sales_data_sample.csv" , encoding="latin1")
data = {
    'Name': ['John', 'Jane', 'Jim'],
    'Age': [28, 34, 29],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

print('Display the info of data set')

print(df.info())
