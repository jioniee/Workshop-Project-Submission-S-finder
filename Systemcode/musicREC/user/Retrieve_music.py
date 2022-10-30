import json
from user.models import Userinfo,Emojidata, Usermusic, Musicdata, Singerdata
import jieba.analyse as analyse
import pandas as pd
import random


def is_all_chinese(strs):
    for i in strs:
        if not '\u4e00' <= i <= '\u9fa5':
            return False
    return True

# def emotion_count(self, text) -> Emotions:
#     emotions = empty_emotions()
#
#     keywords = jieba.analyse.extract_tags(text, withWeight=True)
#
#     for word, weight in keywords:
#         for w in self._find_word(word):
#             emotions[w.emotion] += w.intensity * weight
#
#     return emotions

def emojiAnalysis(sentence):
    emojisarrays = [0] * 21
    emojidata = Emojidata.objects.all()
    # wordlist =
    # for obj in emojidata:

    keywords = analyse.extract_tags(sentence, 50, withWeight=True)
    for keyword,weight in keywords:
        for obj in emojidata:
            if keyword == obj.name:
                if obj.emoji == 'PA':
                    emojisarrays[0] += emojisarrays[0] + obj.weight * weight
                if obj.emoji == 'PE':
                    emojisarrays[1] += emojisarrays[1] + obj.weight* weight
                if obj.emoji == 'PD':
                    emojisarrays[2] += emojisarrays[2] + obj.weight* weight
                if obj.emoji == 'PH':
                    emojisarrays[3] += emojisarrays[3] + obj.weight* weight
                if obj.emoji == 'PG':
                    emojisarrays[4] += emojisarrays[4] + obj.weight* weight
                if obj.emoji == 'PB':
                    emojisarrays[5] += emojisarrays[5] + obj.weight* weight
                if obj.emoji == 'PK':
                    emojisarrays[6] += emojisarrays[6] + obj.weight* weight
                if obj.emoji == 'NA':
                    emojisarrays[7] += emojisarrays[7] + obj.weight* weight
                if obj.emoji == 'NB':
                    emojisarrays[8] += emojisarrays[8] + obj.weight* weight
                if obj.emoji == 'NJ':
                    emojisarrays[9] += emojisarrays[9] + obj.weight* weight
                if obj.emoji == 'NH':
                    emojisarrays[10] += emojisarrays[10] + obj.weight* weight
                if obj.emoji == 'PF':
                    emojisarrays[11] += emojisarrays[11] + obj.weight* weight
                if obj.emoji == 'NI':
                    emojisarrays[12] += emojisarrays[12] + obj.weight* weight
                if obj.emoji == 'NC':
                    emojisarrays[13] += emojisarrays[13] + obj.weight* weight
                if obj.emoji == 'NG':
                    emojisarrays[14] += emojisarrays[14] + obj.weight* weight
                if obj.emoji == 'NE':
                    emojisarrays[15] += emojisarrays[15] + obj.weight* weight
                if obj.emoji == 'ND':
                    emojisarrays[16] += emojisarrays[16] + obj.weight* weight
                if obj.emoji == 'NN':
                    emojisarrays[17] += emojisarrays[17] + obj.weight* weight
                if obj.emoji == 'NK':
                    emojisarrays[18] += emojisarrays[18] + obj.weight* weight
                if obj.emoji == 'NL':
                    emojisarrays[19] += emojisarrays[19] + obj.weight* weight
                if obj.emoji == 'PC':
                    emojisarrays[20] += emojisarrays[20] + obj.weight* weight
    return emojisarrays

# def musicemoji():
    music_file = open('../static/music.json', encoding="utf8")
    for line in music_file:
        if not line:
            continue
        item = json.loads(line)
        # print(item)

        song = item['song']
        singer = item['singer']
        lyric = item['geci']
        # print(singer)
        # print(lyric)

        break

    zeroindex = random.sample(range(0, 20), 21)
    print(zeroindex)



def musicemoji(song, singer, lyric):
        # save obly chinese song.
    if is_all_chinese(song):
        totalemoji = [0] * 21
        if lyric:
            for sentence in lyric:
                emojiarray = emojiAnalysis(sentence)
            for i in range(len(totalemoji)):
                totalemoji[i] += emojiarray[i]
            # print(totalemoji)


            allSinger = []
            for obj in Singerdata.objects.all():
                allSinger.append(obj.singer)
            # print(allSinger)
    #       if user not in database, create a user

            if singer not in allSinger:
                Singerdata.objects.create(singer = singer, PA=0,PE=0,PD=0,PH=0,PG=0,PB=0,PK=0,NA=0,NB=0,NJ=0,
                                          NH=0,PF=0,NI=0,NC=0,NG=0,NE=0,ND=0,NN=0,NK=0,NL=0,PC=0)

            retrieved_singer =  Singerdata.objects.filter(singer = singer).first()
            PA = retrieved_singer.PA + totalemoji[0]
            PE = retrieved_singer.PE + totalemoji[1]
            PD = retrieved_singer.PD + totalemoji[2]
            PH = retrieved_singer.PH + totalemoji[3]
            PG = retrieved_singer.PG + totalemoji[4]
            PB = retrieved_singer.PB + totalemoji[5]
            PK = retrieved_singer.PK + totalemoji[6]
            NA = retrieved_singer.NA + totalemoji[7]
            NB = retrieved_singer.NB + totalemoji[8]
            NJ = retrieved_singer.NJ + totalemoji[9]
            NH = retrieved_singer.NH + totalemoji[10]
            PF = retrieved_singer.PF + totalemoji[11]
            NI = retrieved_singer.NI + totalemoji[12]
            NC = retrieved_singer.NC + totalemoji[13]
            NG = retrieved_singer.NG + totalemoji[14]
            NE = retrieved_singer.NE + totalemoji[15]
            ND = retrieved_singer.ND + totalemoji[16]
            NN = retrieved_singer.NN + totalemoji[17]
            NK = retrieved_singer.NK + totalemoji[18]
            NL = retrieved_singer.NL + totalemoji[19]
            PC = retrieved_singer.PC + totalemoji[20]

            Singerdata.objects.filter(singer = singer).update(PA=PA,PE=PE,PD=PD,PH=PH,PG=PG,PB=PB,PK=PK,NA=NA,NB=NB,NJ=NJ,
                                          NH=NH,PF=PF,NI=NI,NC=NC,NG=NG,NE=NE,ND=ND,NN=NN,NK=NK,NL=NL,PC=PC)

            print("singer : ", singer)
            print(" PA : ", PA)
            print(" PE : ", PE)
            print(" PD : ", PD)
            print(" PH : ", PH)


# print(music_file)
# music_data = json.load(music_file)
# print(music_data)