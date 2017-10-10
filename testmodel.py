import gensim
model = gensim.models.Word2Vec.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)
s = ['hahaha','computer']
for ss in s:
	if ss in model:
		print model[ss]
	else:
		print 0
