# %%
import pandas as pd
from ast import literal_eval

# %%

nft_df = pd.read_csv('./data/data.csv')

attribute_values_df = pd.read_csv('./data/attributes_values_meta.csv')

attribute_type_df = pd.read_csv('./data/attributes_types_meta.csv')

# %%

print(nft_df.head())

print(attribute_values_df.head())

print(attribute_type_df.head())

# %%

attributes = {}

attributes_values = {}

attributes_types = {}

attributes_rarity = {}

attributes_count = {}

left_and_right_same = {}

left_and_right_same_count = 0

nfts = []

# get all the nfts into nft list

for index, row in nft_df.iterrows():

    attributes_temp = literal_eval(row['attributes'])

    nfts.append(
        [row['name'], attributes_temp, row['image'], row['rarity score']])

# %%

for index, row in attribute_type_df.iterrows():

    attributes_types[row['trait_type']] = row['multiplier']

# %%

for index, row in attribute_values_df.iterrows():

    attribute_mutliplier = float(attributes_types[row['trait_type']]) if row[
        'trait_type'] in attributes_types and row['value'] != 'None' else 1

    attributes_rarity[
        str(row['trait_type'] + '_' + str(row['value'])
            )] = row['rarity'] * attribute_mutliplier * row['multiplier']

# %%

print(attributes_rarity)
# %%

for index, row in nft_df.iterrows():

    attributes_temp = literal_eval(row['attributes'])

    total_rarity = 0

    for attribute in attributes_temp:
        search_key = str(attribute['trait_type'] + '_' +
                         str(attribute['value']))

        if search_key in attributes_rarity:

            total_rarity += attributes_rarity[search_key]

    if (total_rarity == 0):
        continue

    nft_df.at[index, 'rarity score'] = total_rarity

# %%

nft_df.sort_values(by=['rarity score'], inplace=True, ascending=False)

nft_df.reset_index(drop=True, inplace=True)

nft_df['rank'] = nft_df.index + 1

# nft_df.drop(columns=['index'], inplace=True)

nft_df.to_csv('./data/data.csv', index=False)
# %%
