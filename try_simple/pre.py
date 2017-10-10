import gensim
modelpath = "/home/jalen/github/AITeamProject/model"
model = gensim.models.Word2Vec.load_word2vec_format(modelpath + '/'+'GoogleNews-vectors-negative300.bin.gz', binary=True)
model.save("gmodel")