# basic nltk example


import nltk
from sklearn.feature_extraction.text import TfidfVectorizer

if __name__ == "__main__":
	sometext = "a b c d e f g h a b c h i j k l m a b"

	tokens = nltk.word_tokenize(sometext)
	print()
	print('tokens:', tokens)
	print()

	fd = nltk.FreqDist(tokens)
	print('frequency distribution:', fd)
	print()


	print('How to use tf-idf: what is unique about each document?')
	docs = [
		'Hello you are my friend world.',
		'This is a test called hello world.',
		'why would i use this test?'
		]

	tok_docs = [nltk.word_tokenize(doc) for doc in docs]
	print()
	print('start with tokenized docs:', tok_docs)
	print()
	print('(pretend each sentence is a doc)')
	print()
	
	#tfidf = TfidfVectorizer(tokenizer=nltk.word_tokenize, stop_words='english')
	#response = tfidf.transform(docs)
	#feature_names = response.get_feature_names()
	#print([feature_names[col] + response[0,col] in response.nonzero()[1]])
	#print(feature_names)

	
	from sklearn.feature_extraction.text import CountVectorizer

	vectorizer = CountVectorizer(min_df=1)
	print(vectorizer)
	print()
	X = vectorizer.fit_transform(docs)
	print(X)
	print(X.toarray())
	print()

	print(vectorizer.get_feature_names())
	print()


	from sklearn.feature_extraction.text import TfidfTransformer
	transformer = TfidfTransformer(smooth_idf=False)
	print(transformer)
	tfidf = transformer.fit_transform(X)
	print(tfidf.toarray())

	# make a list of dicts
	wordlist = list(vectorizer.get_feature_names())
	print(wordlist)
	tfidf_lookup = tfidf.toarray()
	scores = list()
	dontuse = ['.','a','i','?']
	for i in range(len(docs)):
		docscores = dict()
		for word in nltk.word_tokenize(docs[i]):
			if word not in dontuse:
				wordind = wordlist.index(word.lower())
				score = tfidf_lookup[i][wordind]
				docscores[word] = score
		scores.append(docscores)

	print()
	print(scores)
	print()
				
