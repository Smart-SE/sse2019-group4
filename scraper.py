"""
Task    : #5 Keywordに対して、適切なページ（URL）を決定する
version : 0.0.3
author  : da-okazaki
date    : 2019.07.11
"""

import feedparser
import urllib.parse
import os
import json
import pprint
import time

input_path = "./data/keyword"
output_path = "./data/url"

while True:
    start = time.time()
    # ファイル存在チェック
    if (os.path.exists(input_path)):   

        # テキストから文字を抽出
        f = open(input_path)
        keyword = f.read()
        f.close()
        
        # 抽出後ファイル削除
        os.remove(input_path)

        # US1 (キーワードあり)
        if (keyword != "") :
            # URL Encoding
            s_quote = urllib.parse.quote(keyword)

            # Google News Parse
            url = "https://news.google.com/news/rss/search/section/q/" + s_quote + "/" + s_quote + "?ned=jp&amp;hl=ja&amp;gl=JP"
            d = feedparser.parse(url)
            news = list()

            for i, entry in enumerate(d.entries, 1) :
                p = entry.published_parsed
                sortkey = "%04d%02d%02d%02d%02d%02d" % (p.tm_year, p.tm_mon, p.tm_mday, p.tm_hour, p.tm_min, p.tm_sec)
                tmp = {
                    "no": i,
                    "title": entry.title,
                    "link": entry.link,
                    "published": entry.published,
                    "sortkey": sortkey
                }
                news.append(tmp)
                
                if (tmp["no"] == 1) :
                    # OutputFile Create
                    f = open(output_path,'w')
                    # URL Description
                    f.write(entry.link)
                    f.close()
                    break

            news = sorted(news, key=lambda x: x['sortkey'])
            #pprint.pprint(news)


        # US2 (キーワード無し : TOPICS)
        elif (keyword == "") :

            # Google News Parse
            url = "https://news.google.com/rss?hl=ja&gl=JP&ceid=JP:ja"
            d = feedparser.parse(url)
            news = list()
            
            for i, entry in enumerate(d.entries, 1) :

                p = entry.published_parsed
                sortkey = "%04d%02d%02d%02d%02d%02d" % (p.tm_year, p.tm_mon, p.tm_mday, p.tm_hour, p.tm_min, p.tm_sec)
                tmp = {
                    "no": i,
                    "title": entry.title,
                    "link": entry.link,
                    "published": entry.published,
                    "sortkey": sortkey
                }
                news.append(tmp)

                if (tmp["no"] == 1) :
                    # OutputFile Create
                    f = open(output_path,'w')
                    # URL Description
                    f.write(entry.link)
                    f.close()
                    break

            news = sorted(news, key=lambda x: x['sortkey'])
            #pprint.pprint(news)

    else :
        print ("file not exist")

    end = time.time()
    try:
        time.sleep(15-(end-start))
    except ValueError:
        print("scraper.py took 15+ seconds. Skip sleep.")
