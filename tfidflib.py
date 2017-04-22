# has some tfidf functions


import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

def getscores(docs):

	vectorizer = CountVectorizer(min_df=1)
	transformer = TfidfTransformer(smooth_idf=False)

	# count occurrence and calculate tfidf
	X = vectorizer.fit_transform(docs)
	tfidf = transformer.fit_transform(X.toarray())

	# see some random junk
	#print(X.toarray())
	#print(vectorizer.get_feature_names())
	#print(tfidf.toarray())

	# make a list of score dictionaries
	wordlist = list(vectorizer.get_feature_names())
	#print(wordlist)
	tfidf_lookup = tfidf.toarray()
	scores = list()
	dontuse = ['.','a','i','?',"'s","'"] + nltk.corpus.stopwords.words('english')
	for i in range(len(docs)):
		docscores = dict()
		for word in nltk.word_tokenize(docs[i]):
			#if word not in dontuse:
			if word in wordlist:
				wordind = wordlist.index(word.lower())
				score = tfidf_lookup[i][wordind]
				docscores[word] = score
		scores.append(docscores)

	return scores
	
                           
