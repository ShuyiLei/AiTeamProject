# -*- coding: utf-8 -*-
import gensim
import numpy as np
import scipy
import re
import csv
import nltk

def w2v(lst):
	res = np.zeros(300)
	for x in lst:
		if x == '':
			continue
		if x in model:
			res = res + np.array(model[x])
		#elif x in model2:
			#res = res + np.array(model2[x])
	return res

def w2v2(lst):
	res = np.zeros(1000)
	for x in lst:
		if x == '':
			continue
		if x in model2:
			res = res + np.array(model2[x])
		#elif x in model2:
			#res = res + np.array(model2[x])
	return res


def cosine(x,y):
	if  np.any(x) and np.any(y):
		return scipy.spatial.distance.cosine(x,y)
	else:
		return 1

#modelpath = raw_input("Please input the PATH to model folder") or "/home/jalen/github/AITeamProject/model"
modelpath = "/home/jalen/github/AITeamProject/model"
model = gensim.models.Word2Vec.load_word2vec_format(modelpath + '/'+'GoogleNews-vectors-negative300.bin.gz', binary=True)
#model =  gensim.models.Word2Vec.load('gmodel')
model2 = gensim.models.Word2Vec.load_word2vec_format(modelpath + '/'+'freebase-vectors-skipgram1000.bin.gz', binary=True)
english_stopwords = nltk.corpus.stopwords.words('english')
st = nltk.stem.lancaster.LancasterStemmer()
with open(modelpath + '/'+'validation_set.tsv') as f:
	with open('res.tsv','w+') as g:
		reader = csv.reader(f,delimiter='\t')
		reader.next()
		g.write("id,correctAnswer\n")
		for row in reader:
			#g.write(row[0]+',A\n')
			quesp = re.sub(r"[^a-z0-9 \']", " ", row[1].lower()).split(" ")
			answerp = [re.sub(r"[^a-z0-9 \']", " ", row[i+2].lower()).split(" ") for i in range(4)]
			ques = [st.stem(x) for x in quesp if not x in english_stopwords]
			answer = [[st.stem(x) for x in y if not x in english_stopwords] for y in answerp]
			vq = w2v(ques)
			vq2 = w2v2(ques)
			va = [w2v(x) for x in answer]
			va2 = [w2v2(x) for x in answer]
			coss1 =[cosine(vq,x) for x in va]
			coss2 = [cosine(vq2,x) for x in va2]
			coss = [coss1[i] + 0.5 * coss2[i] for i in range(4)]
			ress = coss.index(min(coss))
			al = chr(ress + 65)
			g.write(row[0]+','+al+'\n')
			#print row[0]+','+al
			if np.any(vq2):
				print row[0] +"is zero"
			for i in range(4):
				if not np.any(va[i]):
					print row[0] + "blank"+str(i)





