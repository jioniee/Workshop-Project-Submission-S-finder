# 1. 发送请求
import json
from typing import re

from django.contrib.sites import requests
url = ""
response = requests.get(url=url)
# <Response [200]>: 请求成功
# 2. 获取数据
html_data = response.text
print(html_data)
# 3. 解析数据
# 音乐id 音乐名称 获取下来
# 正则
# <li><a href="/song\?id=(.*?)">(.*?)</a></li>
music_info = re.findall('<li><a href="/song\?id=(.*?)">(.*?)</a></li>', html_data)
for info in music_info:
    music_id = info[0]
    music_name = info[1]
    print(music_id)
    # 找不到的 别人写的代码里面抠出来
    music_url = f'http://music.163.com/song?id={music_id}'
    music_name = re.sub('[\\/:*?"<>|]', '', music_name)
    print(music_url)
    lyric_url = f'http://music.163.com/api/song/media?id={music_id}'
    # 4. 保存数据
    music_data = requests.get(url=music_url).content
    music_data = music_data.decode('utf-8')
    print("This music is: ")
    print(music_info)
    # print(html_data)


    lyric_data = requests.get(url=lyric_url).content
    lyric_data = lyric_data.decode('utf-8')
    lyric_data = json.loads(lyric_data, strict=False)
    lyric_data = lyric_data['lyric']
    lyric_data = lyric_data.replace("\n","")
    lyric_data = lyric_data.replace("\r", "")
    start = False
    whole_lyric = ""
    for i in range(len(lyric_data)):
        if lyric_data[i] == '[':
            whole_lyric += ","
            start = False
        if start and lyric_data[i] != ' ':
            whole_lyric += lyric_data[i]
        if lyric_data[i] == ']':
            start = True
    print(whole_lyric)

    import jieba

    seg_list = jieba.cut(whole_lyric, cut_all=False)
    print("Default Mode: " + "/ ".join(seg_list))

    # with open(f'music/{music_name}.mp3', mode='wb', encoding="utf-8") as f:
    #     f.write(music_data)
    break











