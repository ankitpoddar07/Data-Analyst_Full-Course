import pandas as pd

data = {
    'Name': ['Johny', 'Jane', 'Jim', 'Jack', 'Jill', 'Jerry', 'Jasmine'],
    'Age': [28, 34, 29, 42, 31, 25, 30],
    'Salary': [50000, 60000, 55000, 70000, 62000, 48000, 52000],
    'Experience': [5, 10, 7, 15, 8, 3, 6],
    'Performance': ['Good', 'Excellent', 'Average', 'Outstanding', 'Good', 'Average', 'Excellent'],
    'Department': ['HR', 'Finance', 'IT', 'Marketing', 'Sales', 'IT', 'HR'],   
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'San Diego', 'Dallas'],
    
}

df = pd.DataFrame(data)
print(df)
# Removing a DataFrame Column
# .drop() method  --------------------------   df.drop(columns = ['Column_ Name'], inplace = True)
print('MODIFIED DATAFRAME')
df.drop(columns = ['Performance'], inplace = True)
print(df)

# Removing multiple columns
# df.drop(columns = ['Column_ Name1', 'Column_ Name2'], inplace = True)