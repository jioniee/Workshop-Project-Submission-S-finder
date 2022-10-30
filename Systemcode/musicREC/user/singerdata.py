import json

music_file = open('../static/music.json', encoding="utf8")
for line in music_file:
    if not line:
        continue
    item = json.loads(line)
    print(item)

    song = item['song']
    singer = item['singer']
    lyric = item['geci']
    print(singer)
    print(lyric)

    break


