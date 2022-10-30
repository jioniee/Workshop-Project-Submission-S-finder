"""
[课题]: Python爬取 网易云音乐(评论, 歌词)

[课程时间]: 20:05

[授课老师]: 青灯教育-巳月

[知识点]:
    爬虫基本流程
    requests的使用
    正则表达式的使用

[开发环境]:
    解释器: python 3.8
    编辑器: pycharm 2021.2 专业版
    requests >>> pip install requests

先听一下歌, 等一下后面进来的同学, 20:05开始讲课 有什么喜欢听的歌 也可以发在公屏上

[没听懂?]
课后的回放录播资料找助理老师: python10010
+python安装包 安装教程视频
+pycharm 社区版  专业版 及 激活码免费

零基础 0
有基础 1

爬虫基础:
    批量采集数据(文本 (二进制数据 音乐 视频 图片))
原理:
    模拟 浏览器(客户端) 向 服务器 发送 网络请求(索要数据)

爬虫:
    数据来源分析 https://music.163.com/discover/toplist

代码实现
    1. 发送请求
    2. 获取数据
    3. 解析数据
    4. 保存数据
http://music.163.com/song/media/outer/url?id=254039
"""
import json
# from Retrieve_music import is_all_chinese
import urllib

import requests     # 发送请求 第三方模块
import re           # 内置模块 无需安装

#
import requests
from bs4 import BeautifulSoup
#获取音乐信息
def get_music():
    url = 'http://music.163.com/playlist?id=7193408305'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    res = response.read().decode('utf-8')

    # res = requests.get(url,headers=headers)
    res_text = res
    music_soup = BeautifulSoup(res_text,'html.parser')
    music_list = music_soup.find('ul',class_="f-hide").find_all('a')
    print(music_list)
    for music in music_list:
        print (music)
        song_name = music.text
        print(song_name)
        song_id = music['href'][9:]
        music_url = f'http://music.163.com/song?id={song_id}'
        lyric_url = f'http://music.163.com/api/song/media?id={song_id}'
        # url2 = 'http://music.163.com/song/media/outer/url?id='+song_id+'.mp3'
        # song = requests.get(url2,headers = headers)
        # print(song)
        # r = song
        # with open(name+'.mp3','wb') as f:
        #     f.write(r.content)
        #  is all chinese
        # lyric_data = requests.get(url=lyric_url).content
        request = urllib.request.Request(url=lyric_url, headers=headers)
        response = urllib.request.urlopen(request)
        lyric_data = response.read().decode('utf-8')
        # lyric_data = lyric_data.decode('utf-8')

        lyric_data = json.loads(lyric_data, strict=False)
        lyric_data = lyric_data['lyric']
        lyric_data = lyric_data.replace("\n", "")
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

        formated_lyric = []
        temp = ""
        for i in range(len(whole_lyric)):
            if whole_lyric[i] == ",":
                if temp != "":
                    formated_lyric.append(temp)
                temp = ""
            else:
                temp += whole_lyric[i]
        # print(whole_lyric)
        print(formated_lyric)




get_music()

# # # # # # # # # # # # # # # # # # # # # # # # # # #
# x = 1
url = 'https://music.163.com/#/playlist?id=7193408305'

def create_request(link):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }

    url = link

    request = urllib.request.Request(url = url, headers=headers)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

content = get_content(create_request(url))
# print(content)



import requests     # 发送请求  第三方模块 额外安装的
import execjs       # 调用js的  第三方模块


class Music163():
    def __init__(self):
        # 伪装
        self.headers = {
            # user-agent: Python / requests
            'cookie': '_ntes_nnid=49aa1abc7cac2e3aefcfaa5576fc837c,1642427193866; _ntes_nuid=49aa1abc7cac2e3aefcfaa5576fc837c; NMTID=00OVtn2_ntHUxNdLk8CjO8P6q31bh8AAAF-aEoaDg; WEVNSM=1.0.0; WNMCID=rmsnsq.1642427193981.01.0; WM_TID=nLw51%2BEbIZhBRAQRVEZvvGyQcclCnmG5; ntes_kaola_ad=1; MUSIC_U=ef63db2826f2c58d750719abd63a4be1d730fe3dcfd8c3665f8666226e749962993166e004087dd30179965e6b3ba588386c1530a5aebbcd290a29e290f6160e94359c2a70715816a0d2166338885bd7; _iuqxldmzr_=32; timing_user_id=time_UED7VAa5Ds; __csrf=c03cd4c58e98eec2839f8317c55e43c3; WM_NI=a5Re6BcnujY6KYBlxk6%2BhZXwv7zXXeStYRQE5iG6iNHbePyypVa8a%2BjJRQuOJHTLhavBQfI%2FwXqm6sg9xDqkiP%2FeCCfLkpnG5C5iGwK5w%2FTiQLQTp8fmafYQZv4XhjWbWDI%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eebad03c949bb89bfc7eb8968fb3d85f879e9a86d44a94e98696ce4d95a9f8bac42af0fea7c3b92aa3eb9e86b54aa1b2bb8bdc3e89878e8dfb61f6f5a8bbdb7db6e9b6b9db6f91ac97b3d44ff7b789d7ec468cbeabb1fc73b48aafd9e421aa969eb2f8458a989cadeb6bb69e9f87cc25b588bf8eb579a5e7b8a5f461ab90e186c249a694a591ed4df79dfb8ac67d89ebb9d0d76393949fb5f334a6b3af87dc5b9aaafcb9eb6295be99a5cc37e2a3; playerid=90728715; JSESSIONID-WYYY=RIoybmIW%2B%2BW4Upd5WOwqW9zaNAFX284iru3mQnw%2B85D2N%2Fd5uXTaxrB7t4%2F7VmoWj3fS6SUczlt5NxOVvtsg6SPZKUezFReiys%2FURinPkNokKN%5CkCk6VWHgn%2BvS4pQ79Pe8glDxqE2I0%5CUKyjs9SF3b1x%5Cz6flZYU8SZYS9uonhvSCwT%3A1653484272671',
            'origin': 'https://music.163.com',
            'referer': 'https://music.163.com/search/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
        }
        js = open('music163.js', 'r', encoding='utf-8').read()
        self.ctx = execjs.compile(js)

    def search(self, keyword):
        """
        搜索功能
        :param keyword: 搜索的关键词
        :return:
        """
        url = 'https://music.163.com/weapi/cloudsearch/get/web?csrf_token=c03cd4c58e98eec2839f8317c55e43c3'
        result = self.ctx.call('search', keyword)
        data = {
            "params": result['encText'],
            "encSecKey": result['encSecKey']
        }
        response = requests.post(url=url, data=data, headers=self.headers)
        return response.json()

    def get_music(self, music_id):
        """
        获取音乐
        :param music_id: 音乐id
        :return:
        """
        url = 'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token=c03cd4c58e98eec2839f8317c55e43c3'
        result = self.ctx.call('music', music_id)
        data = {
            "params": result['encText'],
            "encSecKey": result['encSecKey']
        }
        response = requests.post(url=url, data=data, headers=self.headers)
        return response.json()

    def get_comments(self, music_id, page):
        """
        获取歌曲评论
        :param music_id: 歌曲id
        :param page: 页码
        :return:
        """
        url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token=c03cd4c58e98eec2839f8317c55e43c3'
        result = self.ctx.call('comment', music_id, page)
        data = {
            "params": result['encText'],
            "encSecKey": result['encSecKey']
        }
        response = requests.post(url=url, data=data, headers=self.headers)
        return response.json()

    def get_lyric(self, music_id):
        """
        获取歌词
        :param music_id: 歌曲id
        :return: 歌词
        """
        url = 'https://music.163.com/weapi/song/lyric?csrf_token=c03cd4c58e98eec2839f8317c55e43c3'
        result = self.ctx.call('lyrics', music_id)
        data = {
            "params": result['encText'],
            "encSecKey": result['encSecKey']
        }
        response = requests.post(url=url, data=data, headers=self.headers)
        return response.json()

if __name__ == '__main__':
    print("end")
    # music = Music163()
    # print(music.get_music('65766'))
    # print(music.search('陈奕迅'))
    # print(music.get_comments('65766', '1'))
    # print(music.get_lyric('65766'))