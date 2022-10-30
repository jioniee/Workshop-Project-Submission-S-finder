import urllib.request

from bs4 import BeautifulSoup
import requests
from lxml import etree
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options #不显示页面
import time

def get_music(url):
    # opt = Options()
    # opt.add_argument('--headless')
    # opt.add_argument('--disable-gpu')
    # web = Chrome(options=opt)
    # web.get(url)
    # text = web.page_source
    # print(text)

    url = "https://music.163.com/#/playlist?id=7193408305"
    beforeurl = ""
    afterurl = ""
    newurl = ""
    for i in range(len(url)):
        if url[i] == "#":
            newurl = url[:i] + url[i+2:]
            break



    print(newurl)
    print("done")
    url = newurl
    # url = "https://music.163.com/playlist?id=7193408305"
    headers = {
        'Referer': 'http://music.163.com/',
        'Host': 'music.163.com',
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    }

    # s = requests.session()
    # response = s.get(url, headers=headers).content
    # # print(response) 整个html源文件
    # s = BeautifulSoup(response, 'lxml')
    # # print(s)
    # main = s.find('ul', {'class': 'f-hide'})
    # print(main)


    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    res = response.read().decode('utf-8')
    res_text = res
    # res = requests.get(url,headers=headers)

    print (res_text)
    music_soup = BeautifulSoup(res_text, 'html.parser')
    music_list = music_soup.find('ul', class_="f-hide").find_all('a')
    print(music_list)

get_music("https://music.163.com/playlist?id=7193408305")