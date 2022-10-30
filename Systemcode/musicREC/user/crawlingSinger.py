import csv
import requests
from bs4 import BeautifulSoup

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}

key_ids = {1001:"华语男歌手", 1002:"华语女歌手",1003:"华语组合或乐队", 2001:"欧美男歌手", 2002:"欧美女歌手", 2003:"欧美组合或乐队",6001:"日本男歌手",6002:"日本女歌手",6003:"日本组合或乐队",7001:"韩国男歌手",7002:"韩国女歌手",7003:"韩国组合或乐队",4001:"其他男歌手",4002:"其他女歌手", 4003:"其他组合或乐队"}

ids = [1001, 1002, 1003, 2001, 2002, 2003, 6001, 6002, 6003, 7001, 7002, 7003, 7004]

initials = [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 0]

base_url = "https://music.163.com/discover/artist/cat?id={}&initial={}"


for id in key_ids.keys():
    with open(file = r'{}.csv'.format(key_ids[id]), encoding = "utf-8", mode = "a") as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(["id", "name"])
        f.close()
        print("正在爬取{}的信息".format(key_ids[id]))
        for initial in initials:
            try:
                with open(file=r'{}.csv'.format(key_ids[id]), encoding="utf-8", mode="a") as f:

                    url = base_url.format(str(id), str(initial))
                    response = requests.get(url, headers = headers)
                    response.encoding = "utf-8"
                    soup = BeautifulSoup(response.text, "html.parser")
                    ul = soup.find("ul", class_ = "m-cvrlst m-cvrlst-5 f-cb")
                    a_s = ul.find_all("a", class_ = "nm nm-icn f-thide s-fc0")
                    for a in a_s:
                        singer_id = a['href'].split('=')[1]
                        singer_name = a.text
                        writer = csv.writer(f, lineterminator='\n')
                        writer.writerow((singer_id, singer_name))
                        print("正在写入{}{}的信息".format(key_ids[id],singer_name))
                    f.close()
            except Exception as e:
                print(e)
                continue
