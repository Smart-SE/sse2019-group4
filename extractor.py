"""
task : #4 TextデータからKeywordを抽出する
"""
import collections
import termextract.japanese_plaintext
import termextract.core
import time

# how to install termextract
# wget http://gensen.dl.itc.u-tokyo.ac.jp/soft/pytermextract-0_01.zip
# unzip pytermextract-0.01.zip
# cd pytermextract-0.01
# python3 setup.py install

while True:
	start = time.time()
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

	# OPT1: show the most common word
	# print (noun_p)

	# OPT2: search for noun in text, based on dict.
	output_word=''
	for word in list.split():
		if word in text:
			output_word += word + ' '

	print (output_word)
	file = open('data/keyword','w')
	file.write(output_word)
	file.close()
	end = time.time()
	try:
		time.sleep(15-(end-start))
	except ValueError:
		print("Oops: extractor.py took 15+ seconds. Skip sleep.")
