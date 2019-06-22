"""
viewerのスタブ
urlファイルが来たら、urlファイルを消す
"""


import time
import random
import os


while (True) :
        
    if os.path.exists("./data/url") :
        # ファイル削除
        os.remove("./data/url")
    
    else :
        time.sleep(1)
