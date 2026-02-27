from bs4 import BeautifulSoup
import requests
import pandas as pd
def crat():
    url = 'https://new-science.ru/globalnye-strujnye-techeniya-nachinajut-smeshhatsya-v-rezultate-globalnogo-potepleniya/'
    response = requests.get(url)
    bs = BeautifulSoup(response.text,"lxml")
    temp = bs.find('div', 'entry-content entry clearfix').find_all('p')
    news_text = ""
    for p in temp:
        news_text += p.text
    return news_text