# -*- coding: utf-8 -*-
import gensim
import numpy as np
import scipy
import re
import csv


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


def cosine(x,y):
	if  np.any(x) and np.any(y):
		return scipy.spatial.distance.cosine(x,y)
	else:
		return 1

#modelpath = raw_input("Please input the PATH to model folder") or "/home/jalen/github/AITeamProject/model"
modelpath = "/home/jalen/github/AITeamProject/model"
model = gensim.models.Word2Vec.load_word2vec_format(modelpath + '/'+'GoogleNews-vectors-negative300.bin.gz', binary=True)
#model =  gensim.models.Word2Vec.load('gmodel')
#model2 = gensim.models.Word2Vec.load_word2vec_format(modelpath + '/'+'freebase-vectors-skipgram1000.bin.gz', binary=True)
with open(modelpath + '/'+'validation_set.tsv') as f:
	with open('res.tsv','w+') as g:
		reader = csv.reader(f,delimiter='\t')
		reader.next()
		g.write("id,correctAnswer\n")
		for row in reader:
			#g.write(row[0]+',A\n')
			ques = re.sub(r"[^a-z0-9 \']", " ", row[1].lower()).split(" ")
			answer = [re.sub(r"[^a-z0-9 \']", " ", row[i+2].lower()).split(" ") for i in range(4)]
			vq = w2v(ques)
			va = [w2v(x) for x in answer]
			coss =[cosine(vq,x) for x in va]
			ress = coss.index(min(coss))
			al = chr(ress + 65)
			g.write(row[0]+','+al+'\n')
			print row[0]+','+al





