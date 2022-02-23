from glob import glob
import requests
import json
import pandas as pd
import numpy as np
from tornado import ioloop,httpclient

# make a new DF
df = pd.DataFrame(columns=['id', 'attributes'])
i=0
def handle_request(response):
    print(response.code)
    global i
    i -=1
    if i == 0:
        ioloop.IOLoop.current().stop()

http_client = httpclient.AsyncHTTPClient()


for p in range(1, 10):
    url = "https://incepthink.mypinata.cloud/ipfs/Qmc2K93S1RgQ17vxWy31LXbaN498vq4XhzT8ux6hJGgvtC/" + str(
        i)
    i += 1
    http_client.fetch(url, handle_request,ioloop.IOLoop.instance().start())


df.to_csv('data.csv', index=False)

