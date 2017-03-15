from nyt import NYT
from multiprocessing import Pool
import itertools
import time


def apithread(yr,mo):
	data = nytapi.get_archive(yr,mo)
	print('Processing mo {}, {}.'.format(mo,yr))
	time.sleep(10)
	return data

if __name__ == '__main__':
	workers = None
	nytapi = NYT()
	years = range(1852,2017)
	months = range(1,12+1)
	yrmo = list(itertools.product(years,months))
	
	if workers is not None:
		with Pool(workers) as p:
			data = p.starmap(nytapi.get_archive, yrmo)
	else:
		data = itertools.starmap(apithread, yrmo)

	print(list(data))
