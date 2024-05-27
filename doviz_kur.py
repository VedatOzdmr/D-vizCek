import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import time


isim = []
fiyat=[]
table = []
counter = 10

header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}

def  connect(): 
    url ="https://www.doviz.com/"
    sayfa = requests.get(url,headers=header)
    html_content=sayfa.content
    soup =bs(sayfa.text,'html.parser')
    for i in (soup.find_all("span",{"class":"name"})):
        isim.append(i.text)
    for j in(soup.find_all("span",{"class":"value"})):
        fiyat.append(j.text)
    for n in list(zip(isim,fiyat)):
        table.append("{}: {}".format(n[0],n[1]))
    df = pd.DataFrame(table)
    df.columns = ['' for _ in df.columns]
    print(df.to_string(index=False))
    df.columns = [col.strip() for col in df.columns]


connect()

   
        

    

























