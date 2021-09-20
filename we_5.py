# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 23:38:20 2021

@author: zedde
"""


import requests
r = requests.get('https://api.github.com/events')

import lxml.html as lh
from bs4 import BeautifulSoup
import time
import pandas as pd

list_of_exchanges = [{"key":'Binance.com', "value": 5},
                     {"key":'Huobi.com', "value": 5},
                     {"key":"Poloniex.com", "value": 5},
                     {"key":"Bitstamp.net", "value": 5}]

#print(list_of_exchanges[0]["key"])

for exchange in list_of_exchanges:
    
    addresses = []
    
    print(exchange)

    for i in range(2, exchange["value"]):
               
        URL = 'https://www.walletexplorer.com/wallet/'+ exchange["key"] +'/addresses?page=' + str(i)
        #print(URL)
        #for proxy in proxies:
        #page = webdriver.request('GET', URL)
        
        page = requests.get(URL)
            
        doc = lh.fromstring(page.content)

        tr_elements = doc.xpath('//tr')
        
        print("page: "+ str(i))
        
        time.sleep(75)
        
    #print("loop counter: " + str(i))
                
        for t in range(len(tr_elements)):
    
            address = str(tr_elements[t][0].text_content())
                
            addresses.append(address)
                        
    del addresses[0]
                
    df = pd.DataFrame(addresses)
    
    df["label"]=exchange["key"]
    
    df.to_csv("/root/plutohash/pluto-server/datasets/scripts/df_"+exchange["key"]+".csv")

#page = requests.get('https://www.walletexplorer.com/wallet/Binance.com/addresses?page=2')

page = requests.get("https://google.com")
