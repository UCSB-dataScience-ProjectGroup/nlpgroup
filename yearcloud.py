

from nyt import NYT
import tfidflib
from wordcloud import WordCloud
import matplotlib.pyplot as plt

from os import listdir
from os.path import isfile, join


def readf(fname):
	with open(fname,'rb') as f:
		r = f.read().decode('utf-8', errors='replace')
	return r

datafiles = [
	('e','headlinesFromExpansion1850to1900'),
	('e','headlinesFromExpansion1900to1950'),
	('e','headlinesFromExpansion1950to2000'),
	('r','headlinesFromRecession1850to1900'),
	('r','headlinesFromRecession1900to1950'),
	('r','headlinesFromRecession1950to2000'),
]



if __name__ == '__main__':
	mypath = 'data/'

	nytapi = NYT()
	wordcloud = WordCloud(collocations=False)

	# use each month as a doc
	#yrz = [(1853,12),(1853,11),(1853,10)]
	#docs = [' '.join([doc['headline']['main'] for doc in nytapi.get_archive(*yrmo)['response']['docs']]) for yrmo in yrz]
	#files = [str(f) for f in listdir(mypath) if isfile(join(mypath, str(f))) and f[0] != '.']
	#files = [df[1] for df in datafiles if df[0] == 'e']
	#files = [df[1] for df in datafiles if df[0] == 'r']
	files = [mypath + df[1] + '.txt' for df in datafiles]

	#print(listdir(mypath))
	docs = [readf(join(mypath,fname)) for fname in files]

	# get tfidf scores from each doc
	scores = tfidflib.getscores(docs)
	
	# print number of tokens used in the tfidf of each doc
	i = 1
	import numpy as np
	for doc in scores:
		fstr = []
		#scz = 1000*np.array(list(doc.values()))
		#print(np.histogram(scz))
		for w in doc.keys():
			fstr += [w,]*int(1000*doc[w])
		wc = wordcloud.generate(' '.join(fstr))
		#plt.imshow(wc)
		plt.imsave(files[i] + '.png',wc)

		print(str(i), 'has', len(doc.keys()), 'different words.')
		i += 1


	#print(scores)
	#print(len(scores))


