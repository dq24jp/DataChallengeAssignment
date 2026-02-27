import pandas as pd


# all data from the csv
raw_data = pd.read_csv("../team01_ecommerce.csv")

# clean data:


data = raw_data
# date strings to date objects
data['date'] = pd.to_datetime(data['date'])

# rows that are missing one or more pieces of data 
missing_rows = data[data.isna().any(axis=1)]

