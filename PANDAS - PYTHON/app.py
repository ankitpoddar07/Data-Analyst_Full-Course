import pandas as pd

# read data from CSV file into a dataframe

df = pd.read_csv("sales_data_sample.csv", encoding="latin1") 

#df = pd.read_csv("Quarterly_Personal_Income_for_State_of_Iowa.csv")

print(df)