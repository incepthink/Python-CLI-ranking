import requests
import json
import pandas as pd
import numpy as np

# make a new DF
df = pd.DataFrame(columns=['id', 'attributes'])

for i in range(1, 10):
    print('Page:', i)
    url = "https://incepthink.mypinata.cloud/ipfs/Qmc2K93S1RgQ17vxWy31LXbaN498vq4XhzT8ux6hJGgvtC/" + str(
        i)
    r = requests.get(url)
    data = json.loads(r.text)
    df.loc[i] = [i, data['attributes']]

df.to_csv('data.csv', index=False)
