import re
import nltk
english_stopwords = nltk.corpus.stopwords.words('english')
st = nltk.stem.lancaster.LancasterStemmer()
continue_line = 0
with open("science_text_books.txt") as f:
	with open("books.txt","w+") as g:
		for line in f:
			if line == '\n':
				if(continue_line>3):
					g.write('\n')
					continue_line = 0
				else:
					continue_line += 1
				continue
			words = re.sub(r"[^a-z0-9 \']", " ", line.lower()).split(" ")
			if(words[0]=='figure'):
				continue;
			newwords = [st.stem(w) for w in words if not w in english_stopwords]
			newline = ' '.join(newwords)
			g.write(newline+'\n')