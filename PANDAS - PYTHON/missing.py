#  step - 1 > ( NaN )  - Not a Number
#  step - 2 > ( None )  - for object data types
#  step - 3 > ( isnull )  - True ( value missing ) False ( value is present )

import pandas as pd

data = {
    'Name': ['Jhony', 'Jane', 'Jim', 'Jack', 'Jill', 'Jerry', 'Jasmine'],
    'Age': [None, 34, 29, 42, 31, 25, 30],
    'Salary': [None, 60000, 55000, 70000, 62000, 48000, 52000],
    'Department': ['None', 'Finance', 'IT', 'Marketing', 'Sales', 'IT', 'HR'],   
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'San Diego', 'Dallas'],
    
}

df = pd.DataFrame(data)
print(df)

# Detecting missing values ------------
# print(df.isnull())  
# print(df.isnull().sum())  # Count of missing values in each column

# deleting rows & missing values -----
# df.dropna(inplace=True)  # Drop rows with any missing values
# print(df)

# filling missing values ------------
# df.fillna(0, inplace=True)  # Fill missing values with 0
# print(df)

# filling with mean, median, mode ----
df['Age'].fillna(df['Age'].mean(), inplace=True)  # Fill missing Age with mean
df['Salary'].fillna(df['Salary'].median(), inplace=True)  # Fill missing Salary with median
print(df)