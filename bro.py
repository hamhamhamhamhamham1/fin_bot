from bs4 import BeautifulSoup
import requests
import pandas as pd
def news():
    dict_news = {"news": [], "links": [], "views": [], "date": []}
    url = 'https://new-science.ru/?s=глобальное+потепление'
    response = requests.get(url)
    bs = BeautifulSoup(response.text,"lxml")
    temp = bs.find_all('div', 'post-details')
    for post in temp:
        dict_news["news"].append(post.find('h2', 'post-title').text)
        dict_news["links"].append(post.find('h2', 'post-title').find('a').get('href'))
        dict_news["date"].append(post.find('span', 'date meta-item tie-icon').text)
        dict_news["views"].append(post.find('span', 'meta-views meta-item').text)
    df_news = pd.DataFrame(dict_news, columns=["news", "links", "views", "date"])
    return df_news