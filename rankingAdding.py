#  temp will add to the main code later
# %%
import pandas as pd

data_pd = pd.read_csv('./data.csv')

# %%
print(data_pd.head())
# %%

#  add a column to display the rank index
data_pd['rank'] = data_pd.index + 1
print(data_pd.head())

# %%

data_pd.to_csv('./data.csv', index=False)
# %%
print(data_pd.head())
# %%
