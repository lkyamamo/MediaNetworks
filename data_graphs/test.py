import pandas as pd

df = pd.DataFrame({'num_legs': [4, 2], 'num_wings': [0, 2]},
                  index=['dog', 'hawk'])

print(df)

for row in df.itertuples():
    print(row.num_legs)