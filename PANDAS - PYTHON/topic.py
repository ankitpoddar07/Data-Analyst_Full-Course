"""
1 - how big is the data
2 - how many columns and rows
3 - what are the column names
4 - what are the data types of each column
5 - shape and columns
"""

import pandas as pd

#df = pd.read_csv("sales_data_sample.csv", encoding="latin1")
data = {
    'Name': ['John', 'Jane', 'Jim', 'Jack', 'Jill', 'Jerry', 'Jasmine'],
    'Age': [28, 34, 29, 42, 31, 25, 30],
    'Salary': [50000, 60000, 55000, 70000, 62000, 48000, 52000],
    'Department': ['HR', 'Finance', 'IT', 'Marketing', 'Sales', 'IT', 'HR'],
    'Experience': [5, 10, 7, 12, 8, 4, 6],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'San Diego', 'Dallas'],
    'Joining_Date': ['2018-01-15', '2016-03-22', '2019-07-30', '2015-11-05', '2017-05-18', '2020-02-10', '2019-09-25'],
}

df = pd.DataFrame(data)
print(df)

print(f'Shape:{df.shape}')
print(f'Columns Names:{df.columns}')