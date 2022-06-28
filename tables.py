import pandas as pd

office_supplies = pd.read_csv('../pandas_basic/P1-OfficeSupplies.csv', index_col=0)

print(office_supplies)
print(office_supplies.shape)
print(office_supplies.head())
