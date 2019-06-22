"""
task : #4 TextデータからKeywordを抽出する
"""
from janome.tokenizer import Tokenizer

with open('data/text_sample',mode='r') as fp:
    text = fp.read()

t = Tokenizer()
tokens = t.tokenize(text)

for token in tokens:
    print (token)
