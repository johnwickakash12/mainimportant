import pandas as pd
# f=open('housing.data')
housing=pd.read_csv("housing.data")
a=housing.describe
print(a)