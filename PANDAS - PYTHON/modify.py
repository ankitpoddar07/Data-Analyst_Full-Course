# adding Columns to a DataFrame

import pandas as pd

data = {
    'Name': ['John', 'Jane', 'Jim', 'Jack', 'Jill', 'Jerry', 'Jasmine'],
    'Age': [28, 34, 29, 42, 31, 25, 30],
    'Salary': [50000, 60000, 55000, 70000, 62000, 48000, 52000],
    'Department': ['HR', 'Finance', 'IT', 'Marketing', 'Sales', 'IT', 'HR'],   
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'San Diego', 'Dallas'],
    
}
df = pd.DataFrame(data)
print(df)
# Adding a new column Square Brackets ( df ["Column Name"] = value )

# df["Bonus Salary"] = df["Salary"] * 0.1
# print(df)

  # ----------------------------------------------------------------------------------------------------------------
# Using insert method
# df.insert(location (loc) -- 3, "Column_Name" -- "Bonus Salary", "Data" -- df["Salary"] * 0.1) )
df.insert(3, "Experience", [5, 10, 7, 12, 8, 4, 6])
print(df)