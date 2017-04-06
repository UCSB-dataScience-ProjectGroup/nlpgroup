# word2vec example using gensim
# 1: make sure gensim is installed; "conda install gensim"
# 2: check out this page: https://radimrehurek.com/gensim/models/word2vec.html


import gensim
import numpy as np

if __name__ == '__main__':
	
	sentences = [
		['a','b','c','d','e','f','g'],
		['f','g','h','i','j','k','l'],
		['f','g','c','i','m','n','o']
	]


	# Word2Vec Function
	# sentences: list of sentences (as lists - tokenized using nltk)
	# size: number of dimensions to vector space
	# min_count: minimum number of occurrences needed to use that word
	# workers: number of parallel processing units
	model = gensim.models.Word2Vec(sentences, size=5, min_count=1, workers=5)


	print(model)
	print('f:', model['f'])
	print('i:', model['i'])
	print('o:', model['o'])

	print('These are all vectors!')
	print('You can also do vector math with them.')

	print('How similar are "f" and "i"? f*i:', np.dot(model['f'],model['i']))
	print()

	print('What is the combination of "f" and "i"? f+i:', model['f'] + model['i'])
	print()







