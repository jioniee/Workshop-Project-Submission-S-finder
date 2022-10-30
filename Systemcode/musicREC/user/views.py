import json
import random
import urllib

from bs4 import BeautifulSoup
from django.contrib.sites import requests
from django.shortcuts import render, HttpResponse, redirect
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

from user.models import Userinfo,Emojidata, Usermusic, Musicdata
from user.Retrieve_music import is_all_chinese,emojiAnalysis,musicemoji,Singerdata
from user.machineREC import get_singerid, get_u_vector, prediction

# Create your views here.
def index(request):
    if request.method == "GET":
        return render(request, 'index.html')

    user = request.POST.get("user")
    link = request.POST.get("link")

    isEmpty = False
    # print(user, " user is ")
    if user == "" or link == "":
        message = "Please fill the blank"
        isEmpty = True
        return render(request, 'index.html', locals())

    df = pd.read_csv("./static/user_singerdata.csv", index_col=[0])
    df.index = range(0, len(df.index.tolist()))

    singer_names = df['singer'].tolist()
    data = df.drop(['singer'], axis=1)
    features = data.columns.tolist()
    data = MinMaxScaler().fit_transform(data)
    data = pd.DataFrame(data)

    url = link
    newurl = ""
    for i in range(len(url)):
        if url[i] == "#":
            newurl = url[:i] + url[i+2:]
            break
    url = newurl

    all_sing_emoji = get_music(url)
    print(all_sing_emoji)
    indices = prediction([all_sing_emoji], data)

    i = 0
    for i in range(len(indices)):
        if i == 0:
            singer1 = df.loc[indices[i], 'singer']
            i +=1
        if i == 1:
            singer2 = df.loc[indices[i], 'singer']
            i +=1
        if i == 2:
            singer3 = df.loc[indices[i], 'singer']
            i +=1
        else:
            break

    randnumlist = random.sample(range(1,35),3)
    randnumber1 = randnumlist[0]
    randnumber2 = randnumlist[1]
    randnumber3 = randnumlist[2]
    img1 = '../static/image/i' + str(randnumber1) + '.jpg'
    img2 = '../static/image/i' + str(randnumber2) + '.jpg'
    img3 = '../static/image/i' + str(randnumber3) + '.jpg'

    link1 = f'https://music.163.com/#/search/m/?s={singer1}&type=100'
    link2 = f'https://music.163.com/#/search/m/?s={singer2}&type=100'
    link3 = f'https://music.163.com/#/search/m/?s={singer3}&type=100'
    print("singer1 : ")
    print(singer1)
    singer1data = Musicdata.objects.all().filter(singer=singer1)
    for i in range(len(singer1data)):
        if i == 0:
            singer1song1 = singer1data[i].name
            print(singer1song1)
            singer1lyric1 = singer1data[i].lyric
            print(singer1lyric1)
            singer1lyric1 = removeString(singer1lyric1)
            singer1lyric1 = singer1lyric1[:15]
            print(singer1lyric1)
        if i == 1:
            singer1song2 = singer1data[i].name
            singer1lyric2 = singer1data[i].lyric
            singer1lyric2 = singer1lyric2[0]
        if i == 2:
            singer1song3 = singer1data[i].name
            singer1lyric3 = singer1data[i].lyric
            singer1lyric3 = singer1lyric3[0]
        else:
            break

    singer2data = Musicdata.objects.all().filter(singer=singer2)
    for i in range(len(singer2data)):
        if i == 0:
            singer2song1 = singer2data[i].name
            singer2lyric1 = singer2data[i].lyric
            singer2lyric1 = singer2lyric1[0]
        if i == 1:
            singer2song2 = singer2data[i].name
            singer2lyric2 = singer2data[i].lyric
            singer2lyric2 = singer2lyric2[0]
        if i == 2:
            singer2song3 = singer2data[i].name
            singer2lyric3 = singer2data[i].lyric
            singer2lyric3 = singer2lyric3[0]
        else:
            break

    singer3data = Musicdata.objects.all().filter(singer=singer3)
    for i in range(len(singer3data)):
        if i == 0:
            singer3song1 = singer3data[i].name
            singer3lyric1 = singer3data[i].lyric
            singer3lyric1 = singer3lyric1[0]
        if i == 1:
            singer3song2 = singer3data[i].name
            singer3lyric2 = singer3data[i].lyric
            singer3lyric2 = singer3lyric2[0]
        if i == 2:
            singer3song3 = singer3data[i].name
            singer3lyric3 = singer3data[i].lyric
            singer3lyric3 = singer3lyric3[0]
        else:
            break

    return render(request, 'recommendation.html', locals())


def recommendation(request):

    return render(request, 'recommendation.html', locals())

def emojidata(request):
    entries = pd.read_csv('./static/lyric_emo.csv')

    for i in range(0, len(entries)):
        word = entries['词语'][i]
        emoji = entries['情感分类'][i]
        weight = entries['强度'][i]

        Emojidata.objects.create(name=word, emoji=emoji, weight=weight)

    return HttpResponse("Emojidata add successfully")

def musicdata(request):
    music_file = open('./static/music.json', encoding="utf8")
    for line in music_file:
        if not line:
            continue
        item = json.loads(line)
        # print(item)

        song = item['song']
        singer = item['singer']
        lyric = item['geci']
        lyric = lyric[:253]
        print(lyric)

        Musicdata.objects.create(name = song, singer = singer, lyric = lyric)
    return HttpResponse("helloworld")


def testemojimusic(request):
    music_file = open('./static/music.json', encoding="utf8")
    i = 0
    for line in music_file:
        print(i)
        if i < 5000:
            if not line:
                continue
            item = json.loads(line)
            # print(item)

            song = item['song']
            singer = item['singer']
            lyric = item['geci']
            print(singer)
            # print(lyric)

            musicemoji(song,singer,lyric)
            # print(emojiMusic)
            i +=1
        else:
            break
    return HttpResponse("helloworld")

def clear(request):
    Singerdata.objects.all().delete()
    Musicdata.objects.all().delete()
    return HttpResponse("delete successfully")


def get_music(url):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    res = response.read().decode('utf-8')

    # res = requests.get(url,headers=headers)
    res_text = res
    print (res_text)
    music_soup = BeautifulSoup(res_text, 'html.parser')
    music_list = music_soup.find('ul', class_="f-hide").find_all('a')
    print(music_list)
    number_analyse = 0
    all_song_emoji = [0] * 21
    for music in music_list:
        this_song_emoji = [0] * 21
        if number_analyse < 10:
            print(music)
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
            if is_all_chinese(song_name):
                number_analyse += 1
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

                # for i in range(len(formated_lyric)):
                if formated_lyric:
                        for sentence in formated_lyric:
                            print("sen: ")
                            print(sentence)
                            emojiarray = emojiAnalysis(sentence)
                        for i in range(len(this_song_emoji)):
                            this_song_emoji[i] += emojiarray[i]

                print("this emoji: ")
                print(this_song_emoji)

                for i in range(len(all_song_emoji)):
                    all_song_emoji[i] += this_song_emoji[i]
    return all_song_emoji

def removeString(lyric):
    newlyric = ""
    if lyric:
        for i in lyric:
            if i == "[" or i == "'" or i == '"':
                i = ""
            newlyric = newlyric + i
        # lyric.replace('g', '')
        # lyric.replace('[', '')
        # lyric.replace("'", '')
        # lyric.replace('"', '')
    return newlyric