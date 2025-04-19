import pandas as pd

data = {
    'Name': ['Johny', 'Jane', 'Jim', 'Jack', 'Jill', 'Jerry', 'Jasmine'],
    'Age': [28, 34, 29, 42, 31, 25, 30],
    'Salary': [50000, 60000, 55000, 70000, 62000, 48000, 52000],
    'Department': ['HR', 'Finance', 'IT', 'Marketing', 'Sales', 'IT', 'HR'],   
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'San Diego', 'Dallas'],
    
}

df = pd.DataFrame(data)
print(df)

# Updating a DataFrame Value
# .loc[] method

#df.loc[row_index, "Column_ Name"] = new_value

# df.loc[0,'Salary'] = 55000
# print(df)

# Updating multiple values Salary increase by 10 %
df['Salary'] = df['Salary'] * 1.10
print(df)