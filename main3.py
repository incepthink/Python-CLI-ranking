# %%
import concurrent.futures
import requests
import pandas as pd
import json
import time
from web3 import Web3, HTTPProvider

out = []
CONNECTIONS = 100

TIMEOUT = 5000

urls = []

attributes = {}

attributes_values = {}

attributes_types = {}

attributes_rarity = {}

attributes_count = {}

left_and_right_same = {}

left_and_right_same_count = 0

nfts = []

id = 0

count = 100

w3 = Web3(HTTPProvider('https://rpc.ftm.tools'))

if (not w3.isConnected()):
    print("Not connected")
    exit()

abi = '[{"inputs":[{"internalType":"string","name":"baseURI","type":"string"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"approved","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[],"name":"MAX_Supply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"credits","type":"uint256"}],"name":"addCredit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address[]","name":"addresses","type":"address[]"}],"name":"addToAllowList","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"},{"internalType":"uint256","name":"quantity","type":"uint256"}],"name":"adminMint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"allowListClaimedBy","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"allowListMaxMint","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOfCredit","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"baseURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getScopeIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"hasPresaleStarted","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"hasSaleStarted","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"numberOfTokens","type":"uint256"}],"name":"mint","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"mintCredit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"numberOfTokens","type":"uint256"}],"name":"mintWhitelist","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"numberOfTokens","type":"uint256"},{"internalType":"uint256","name":"id","type":"uint256"}],"name":"mintWithToken","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"mintedPresaleTokens","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"addr","type":"address"}],"name":"onAllowList","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pausePresale","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"pauseSale","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"price","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address[]","name":"addresses","type":"address[]"}],"name":"removeFromAllowList","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"baseURI","type":"string"}],"name":"setBaseURI","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"startPresale","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"startSale","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenOfOwnerByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_owner","type":"address"}],"name":"tokensOfOwner","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"withdrawAll","outputs":[],"stateMutability":"nonpayable","type":"function"}]'
address = "0x8a89c505d174B056A35faF5d6c712ced921E7B48"

contractCaller = w3.eth.contract(address=address, abi=abi)

# print(contractCaller.functions.ownerOf(8787).call())

for i in range(1, count + 1):
    # print('Page:', i)
    url = "https://incepthink.mypinata.cloud/ipfs/Qmc2K93S1RgQ17vxWy31LXbaN498vq4XhzT8ux6hJGgvtC/" + str(
        i)
    urls.append(url)


def load_url(url, timeout):
    try:
        r = requests.get(url, timeout=timeout)
        data = json.loads(r.text)
        global id

        name = data['name']

        id_local = name.split('#')[-1]

        # try:
        print(id_local)

        contractCaller.functions.ownerOf(int(id_local)).call()
        # except Exception as e:
        # continue

        nfts.append([data['name'], data['attributes'], data['image'], 0])

        attributes_count[len(data['attributes'])] = attributes_count[len(
            data['attributes'])] + 1 if len(
                data['attributes']) in attributes_count else 1

        left_item = None
        right_item = None
        for attribute in data['attributes']:

            if attribute['trait_type'] == 'Left Item':
                left_item = attribute['value']

            if attribute['trait_type'] == 'Right Item':
                right_item = attribute['value']

            attributes_values[attribute['value'] + ' ' +
                              attribute['trait_type']] = attributes_values[
                                  attribute['value'] + ' ' +
                                  attribute['trait_type']] + 1 if (
                                      attribute['value'] + ' ' +
                                      attribute['trait_type']
                                  ) in attributes_values else 1
            attributes_types[attribute['trait_type']] = attributes_types[
                attribute['trait_type']] + 1 if attribute[
                    'trait_type'] in attributes_types else 1

            if attribute['trait_type'] in attributes:
                attributes[attribute['trait_type']].add(attribute['value'])
            else:
                attributes[attribute['trait_type']] = set()
                attributes[attribute['trait_type']].add(attribute['value'])

        if left_item == right_item:

            global left_and_right_same
            global left_and_right_same_count
            left_and_right_same[data['name']] = left_item
            left_and_right_same_count = left_and_right_same_count + 1

    except Exception as e:
        print(e, "Over here")


with concurrent.futures.ThreadPoolExecutor(
        max_workers=CONNECTIONS) as executor:
    future_to_url = (executor.submit(load_url, url, TIMEOUT) for url in urls)
    time1 = time.time()
    for future in concurrent.futures.as_completed(future_to_url):
        try:
            data = future.result()
        except Exception as exc:
            data = str(type(exc))
        finally:
            out.append(data)

            print(str(len(out)), end="\r")

    time2 = time.time()

print(f'Took {time2-time1:.2f} s')

#  convert nfts list to dataframe
nft_df = pd.DataFrame(nfts,
                      columns=['name', 'attributes', 'image', 'rarity score'])

#  drop the first column
# nft_df = nft_df.drop(nft_df.columns[0], axis=1)

# nft_df.reset_index(inplace=True)

# nft_df.set_index('index', inplace=True)

# print(nft_df)

for key, value in attributes_count.items():
    rarity_of_count = value / count
    attributes_rarity['count ' + str(key)] = rarity_of_count

for attribute in attributes:
    # print(attribute, attributes[attribute], attributes_types[attribute],
    #   "xxxx")

    count_for_no_value = count - attributes_types[attribute]

    # print(count_for_no_value)
    # attributes[attribute].add('No Value')

    for value in attributes[attribute]:
        # print(value, attributes_values[value])
        rarity = attributes_types[attribute] / attributes_values[value + ' ' +
                                                                 attribute]
        # print(rarity)
        attributes_rarity[value + ' ' + attribute] = rarity

    attributes_rarity[
        'None' + ' ' +
        attribute] = count / count_for_no_value if count_for_no_value != 0 else 0

for nft in nfts:
    # print(nft)
    total_rarity = 0
    for attribute in attributes:
        found_flag = False

        for atr in nft[1]:
            if (atr['trait_type'] == attribute):
                #    print("found")
                found_flag = True

        if found_flag == False:
            # print("not found",attribute)

            total_rarity += attributes_rarity['None' + ' ' + atr['trait_type']]
            #  add the rarity of the attribute to nft in df
            nft[1].append({'trait_type': attribute, 'value': 'None'})

    for x in nft[1]:
        # print(x)
        total_rarity += attributes_rarity[x['value'] + ' ' + x['trait_type']]

        #  check if attribute exits inside nft[1] 'trait_type'

        # if attribute in nft[1]:
        #     total_rarity += attributes_rarity[nft[1][attribute]['value'] + ' ' +
        #                                      attribute]
        # else:
        #     total_rarity += attributes_rarity['None' + ' ' + attribute]

    count_rarity = 'count ' + str(len(nft[1]))

    total_rarity += attributes_rarity[count_rarity]

    name = nft[0]

    if (name in left_and_right_same):
        total_rarity += count / left_and_right_same_count
        # add the rarity of the attribute to nft in df
        nft[1].append({'trait_type': 'Left Right Same', 'value': True})
    else:
        nft[1].append({'trait_type': 'Left Right Same', 'value': False})

    nft[3] = total_rarity

# added Left Right Same in attribute lists

print(attributes_rarity)

print(attributes_types)

nft_df = pd.DataFrame(nfts,
                      columns=['name', 'attributes', 'image', 'rarity score'])

nft_df.sort_values(by=['rarity score'], ascending=False, inplace=True)

nft_df.reset_index(inplace=True)

nft_df.drop(nft_df.columns[0], axis=1, inplace=True)

nft_df['rank'] = nft_df.index + 1

nft_df.to_csv('./data/data.csv', index=False)

#  save all the trait types to a csv with multiplier set to 1 for each

# %%
attributes_types_df = pd.DataFrame([], columns=['trait_type', 'multiplier'])

for x in attributes_types:
    attributes_types_df = attributes_types_df.append(
        {
            'trait_type': x,
            'multiplier': 1
        }, ignore_index=True)

attributes_types_df = attributes_types_df.append(
    {
        'trait_type': 'Left Right Same',
        'multiplier': 1
    }, ignore_index=True)

print(attributes_types_df)

# %%

# save attributes_types_df to csv sheet 2

attributes_types_df.to_csv('./data/attributes_types_meta.csv', index=False)

# %%

# save all attributes value with multipler and trait type

attributes_values_df = pd.DataFrame(
    [], columns=['trait_type', 'value', 'multiplier', 'rarity'])

for x in attributes:
    for y in attributes[x]:

        rarity = attributes_rarity[y + ' ' + x]

        attributes_values_df = attributes_values_df.append(
            {
                'trait_type': x,
                'value': y,
                'multiplier': 1,
                'rarity': rarity
            },
            ignore_index=True)

attributes_values_df = attributes_values_df.append(
    {
        'trait_type': 'Left Right Same',
        'value': 'None',
        'multiplier': 1,
        'rarity': 0
    },
    ignore_index=True)

attributes_values_df = attributes_values_df.append(
    {
        'trait_type': 'Left Right Same',
        'value': True,
        'multiplier': 1,
        'rarity': count / left_and_right_same_count
    },
    ignore_index=True)

print(attributes_values_df)

attributes_values_df.to_csv('./data/attributes_values_meta.csv', index=False)

# %%
