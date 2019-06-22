"""
Task    : #5 Keywordに対して、適切なページ（URL）を決定する
version : 0.0.1
author  : da-okazaki
date    : 2019.06.22

5-A. キーワードあり : ニュースのURLを取得
5-B. キーワードなし : 一番ホットニュースのURLを取得

"""

import feedparser
import urllib.parse
import os
import json
import pprint

path = "./data/keyword.txt"

# テキストから文字を抽出
f = open(path)
keyword = f.read()
f.close()

# 1. ファイルの存在をチェック
if (os.path.exists(path)):    

    # a. キーワードあり
    if (keyword != "") :
        # URLエンコーディング
        s_quote = urllib.parse.quote(keyword)
        
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

        news = sorted(news, key=lambda x: x['sortkey'])
        pprint.pprint(news)

    # b. キーワードなし
    elif (keyword == "") :
        print("keywordなし")

    # ファイル削除 ./data/keyword.txt
    # ファイル作成 ./data/url.txt