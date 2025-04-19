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

high_salary = df[df['Salary'] > 50000]
print('\nEmployees with Salary greater than 50000')
print(high_salary)

# Filtering rows on multiple conditions &
filtered = (df['Salary'] > 50000) & (df['Age'] > 30)

print(f'Employees list Age >30 + Salary > 50000')
filtered = df[filtered]
print(filtered)

# using OR condition

filtered = (df['Salary'] > 50000) | (df['Experience'] > 5)
print(f'Employees list Experience >5 + Salary > 50000')
filtered = df[filtered]
print(filtered)