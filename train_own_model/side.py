# -*- coding: utf-8 -*-
import gensim
import numpy as np
import scipy
import re
import csv
import nltk


def w2v(lst):
	res = np.zeros(400)
	for x in lst:
		if x == '':
			continue
		if x in model:
			res = res + np.array(model[x])
		#elif x in model2:
			#res = res + np.array(model2[x])
	return res

# def w2v2(lst):
# 	res = np.zeros(1000)
# 	for x in lst:
# 		if x == '':
# 			continue
# 		if x in model2:
# 			res = res + np.array(model2[x])
# 		#elif x in model2:
# 			#res = res + np.array(model2[x])
# 	return res


def cosine(x,y):
	if  np.any(x) and np.any(y):
		return scipy.spatial.distance.cosine(x,y)
	else:
		return 1

#modelpath = raw_input("Please input the PATH to model folder") or "/home/jalen/github/AITeamProject/model"
modelpath = "/home/jalen/github/AITeamProject/model"
#model = gensim.models.Word2Vec.load_word2vec_format(modelpath + '/'+'GoogleNews-vectors-negative300.bin.gz', binary=True)
model =  gensim.models.Word2Vec.load_word2vec_format('books.txt.vector', binary=False)
#model2 = gensim.models.Word2Vec.load_word2vec_format(modelpath + '/'+'freebase-vectors-skipgram1000.bin.gz', binary=True)
english_stopwords = nltk.corpus.stopwords.words('english')
st = nltk.stem.lancaster.LancasterStemmer()
count = 0
correct = 0
with open(modelpath + '/'+'training_set.tsv') as f:
	with open('side.rsv','w+') as g:
		reader = csv.reader(f,delimiter='\t')
		reader.next()
		g.write("id,correctAnswer\n")
		for row in reader:
			#g.write(row[0]+',A\n')
			quesp = re.sub(r"[^a-z0-9 \']", " ", row[1].lower()).split(" ")
			answerp = [re.sub(r"[^a-z0-9 \']", " ", row[i+3].lower()).split(" ") for i in range(4)]
			ques = [st.stem(x) for x in quesp if not x in english_stopwords]
			answer = [[st.stem(x) for x in y if not x in english_stopwords] for y in answerp]
			vq = w2v(ques)
			va = [w2v(x) for x in answer]
			coss =[cosine(vq,x) for x in va]
			#coss = [coss1[i] + 0.5 * coss2[i] for i in range(4)]
			ress = coss.index(min(coss))
			al = chr(ress + 65)
			count += 1
			if(row[2]==al):
				correct += 1
			g.write(row[0]+','+al+" "+row[2]+'\n')
			print row[0]+','+al
		print count
		print correct
		print (correct+0.0)/count





