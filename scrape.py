from bs4 import BeautifulSoup
import requests
import json


def collectProverbs():
    url = "https://www.thebrightc.com/post/100-african-proverbs"
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }
    response = requests.get(url=url,headers=headers)
    soup = BeautifulSoup(response.text,'lxml')
    proverbs = soup.find_all('span',style="color:#1D2D3C")
    proverbs = proverbs[6:-3]
    container = list()
    for proverb in proverbs:
       data = {
        "proverb":proverb.get_text()
       }
       container.append(data)
    return container


proverb = collectProverbs()
with open("prov.json",mode="w") as prov_file:
    json.dump(proverb,prov_file,ensure_ascii=False)