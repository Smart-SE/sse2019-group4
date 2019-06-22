"""
extractorのスタブ
textファイルが来たら、Keywordファイルを置く
"""


import time
import random
import os


while (True) :
        
    if os.path.exists("./data/text") :
        # ファイル削除
        os.remove("./data/text")
    
        textset = [
            '巨人',
            'ベイスターズ',
            'タピオカ',
        ]
        with open('./data/keyword', mode='w') as f:
            f.write(random.choice(textset))


    else :
        time.sleep(1)
