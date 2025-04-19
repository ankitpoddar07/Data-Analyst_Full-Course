import pandas as pd

data = {
    'Name': ['John', 'Jane', 'Jim'],
    'Age': [28, 34, 29],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

# Create a DataFrame from the data
df = pd.DataFrame(data)
print(df)

# Save the DataFrame to a CSV filecls
#df.to_csv('output.csv', index=False)

# Save the DataFrame to an Excel file
#df.to_excel('output.xlsx', index=False)

# Save the DataFrame to a JSON file
#df.to_json('output.json', orient='records', lines=True)