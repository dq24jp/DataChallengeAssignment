import pandas as pd


# all data from the csv
data = pd.read_csv("../team01_ecommerce.csv")

# rows that are missing one or more pieces of data 
missing_rows = data[data.isna().any(axis=1)]
