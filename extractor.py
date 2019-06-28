"""
task : #4 TextデータからKeywordを抽出する
"""
import collections
import termextract.japanese_plaintext
import termextract.core

# how to install termextract
# wget http://gensen.dl.itc.u-tokyo.ac.jp/soft/pytermextract-0_01.zip
# unzip pytermextract-0.01.zip
# cd pytermextract-0.01
# python3 setup.py install


text = open('data/text',encoding='utf-8',mode='r').read()

# TODO: randomly pick up one keyword and print it out
list = open('dict/sports.csv',encoding='utf-8',mode='r').read()

# reference url
# https://qiita.com/EastResident/items/0cdc7c5ac1f0a6b3cf1d
frequency = termextract.japanese_plaintext.cmp_noun_dict(text)
LR = termextract.core.score_lr(frequency,
        ignore_words=termextract.japanese_plaintext.IGNORE_WORDS,
        lr_mode=1,average_rate=1)

term_imp = termextract.core.term_importance(frequency, LR)

data_collection = collections.Counter(term_imp)
noun, value = data_collection.most_common()[0]
noun_p = termextract.core.modify_agglutinative_lang(noun)

list_p = list.replace('\n',' ')
if noun_p in list_p:
	print(noun_p)

# debug
#for cmp_noun, value in data_collection.most_common():
    #print(termextract.core.modify_agglutinative_lang(cmp_noun), value, sep="\t")
    #print(termextract.core.modify_agglutinative_lang(cmp_noun), sep="\t")
