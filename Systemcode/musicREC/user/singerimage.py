import urllib.request


import pandas as pd
from bs4 import BeautifulSoup


def findimage(singer):
    search_url = f'https://music.163.com/#/search/m/?s={singer}&type=100'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
    request = urllib.request.Request(url=search_url, headers=headers)
    response = urllib.request.urlopen(request)
    response = response.read().decode('utf-8')
    print(response)
    music_soup = BeautifulSoup(response, 'html.parser')
    music_list = music_soup.find('div', class_="u-cover u-cover-5").find_all('a')

    print(music_list)

findimage("张学友")