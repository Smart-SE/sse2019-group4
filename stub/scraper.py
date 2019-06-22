"""
scraperのスタブ
keywordファイルが来たら、urlファイルを置く
"""


import time
import random
import os


while (True) :
        
    if os.path.exists("./data/keyword") :
        # ファイル削除
        os.remove("./data/keyword")
    
        textset = [
            'https://www.j-cast.com/2019/06/22360464.html?p=all',
            'https://www.sanspo.com/baseball/news/20190622/gia19062205020005-n1.html',
            'https://www.asahi.com/articles/ASM6L36M5M6LULOB003.html',
        ]
        with open('./data/url', mode='w') as f:
            f.write(random.choice(textset))


    else :
        time.sleep(1)
