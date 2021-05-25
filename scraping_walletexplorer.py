import requests
import lxml.html as lh
from bs4 import BeautifulSoup

page_list = []

for i in range(10):

    URL = 'https://www.walletexplorer.com/wallet/Binance.com/addresses?page=' + str(2)

    page = requests.get(URL)
    
    doc = lh.fromstring(page.content)

    tr_elements = doc.xpath('//tr')
    
    page_list.append(tr_elements)

#Store the contents of the website under doc
doc = lh.fromstring(page.content)
#Parse data that are stored between <tr>..</tr> of HTML
tr_elements = doc.xpath('//tr')

[len(T) for T in tr_elements[:12]]

binance_addresses = []

for i in range(len(tr_elements)):
    
    address = str(tr_elements[i][0].text_content())
    
    binance_addresses.append(address)
    
    
print(tr_elements[1][0].text_content())

address = str(tr_elements[1][0].text_content())


[len(T) for T in tr_elements[:12]]

x = list(str(tr_elements[1]))
print(x)