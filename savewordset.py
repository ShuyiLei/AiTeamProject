import re
import pickle
word_set = set()
i = 0
with open("/common/public/AI_DATA/science_text_books.txt") as f:
	for line in f:
		line = re.sub(r"[^a-z0-9 \']", " ", line.lower())
		word_set = word_set.union(line.split(" "))
		i = i + 1
		print i
with open("ck12wordset", 'wb') as f:
	pickle.dump(word_set, f)
