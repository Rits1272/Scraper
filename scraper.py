from bs4 import BeautifulSoup
import requests
import html5lib
import json


URL = "https://inshorts.com/en/read"
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html5lib')
headlines = soup.findAll('span', attrs = {'itemprop' : 'headline'})
count_headlines = len(headlines)
fh = open("my_json.json", "a+")

def news():
    for i in range(count_headlines):
        #print(headlines[i].text)
       

         
        fh.write(json.dumps({"News": headlines[i].text}))

    fh.close()

a = news()

