import pandas as pd
data=[[1,444,'abc'],
      [2,333,'dsd'],
      [3,555,'dgg'],
      [7,666,'ghj']]
df = pd.DataFrame(data, columns=["colum1", "colum 2","colum3"])
print(df)