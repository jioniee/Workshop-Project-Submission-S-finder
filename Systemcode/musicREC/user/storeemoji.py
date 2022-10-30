import pandas as pd
from user.models import Userinfo,Emojidata, Usermusic, Musicdata

entries =pd.read_csv('../static/lyric_emo.csv')

for i in range(0, len(entries)):
    word = entries['词语'][i]
    emoji = entries['情感分类'][i]
    weight = entries['强度'][i]

    Emojidata.objects.create(name=word, emoji=emoji, weight=weight)

