"""
recognizerのスタブ
15秒に1回ランダムな文字列をファイル出力する
"""

import time
import random

while (True) :
    textset = [
        '巨人が勝ったよね',
        'ベイスターズの本拠地ってどこだっけ？',
        'タピオカミルクティーってこの前飲んだんだけど、すんごいおいしいよね！',
    ]
    with open('./data/text', mode='w') as f:
         f.write(random.choice(textset))
         
    time.sleep(15)