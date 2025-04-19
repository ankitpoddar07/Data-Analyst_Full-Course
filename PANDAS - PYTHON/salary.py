# Step 1: displaying the sample data frame  
import pandas as pd


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

# display the dataframe
print('Sample data frame')
print(df)

# Step 2: Selecting the Single columns to be displayed
print("Names(Sinle column return series)")
name = df['Name']
print(name)

# Step 3: Selecting the Multiple columns to be displayed
subset = df[['Name', 'Salary']]
print('\nSubset with Name and Salary')
print(subset)

# Step 4: Filtering the Rows (rowsfilter.py)