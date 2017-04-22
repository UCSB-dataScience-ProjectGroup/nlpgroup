import http.client
import json
import os
from nltk import word_tokenize



class NYT:

	def __init__(self,config_file='config.json',data_folder='nytapi_data/'):
		self.conn = http.client.HTTPConnection("api.nytimes.com")
		try:
			with open(config_file,'r') as f: #is config.txt a file that needs to be downloaded?
				self.cfg = json.load(f)
		except:
			raise(Exception('Error loading config.json file. Does it exist and is it json?'))

		# data folder
		self.data_folder = data_folder
		#print(os.path.isfile('nytapi_data'))
		if not os.path.isdir(data_folder):
			os.mkdir(data_folder)

	def get_archive(self, year=1851, month=12):
		''' Either gets previously retreived data or makes a new
		request to the nyt api to get archive data for a given 
		year and month.
		'''

		fname = self.data_folder + '{}.{}.json'.format(year,month)
		if os.path.isfile(fname):
			json_string = self.archives_local(year,month,fname)
		else:
			json_string = self.archives_apirequest(year,month)
			with open(fname,'w') as f:
				f.write(json_string)
		
		return json.loads(json_string)
	
	def archives_local(self, year, month, fname):
		# get data from local file
		with open(fname,'r') as f:
			json_string = f.read()
		return json_string


	def archives_apirequest(self, year, month):
		
		# make request to api using get variable "api-key"
		self.conn.request("GET", "//svc/archive/v1/" + str(year) + \
		"/" + str(month) + ".json?api-key=%s" % (self.cfg['apikey'],))
		
		# get response from connection object
		r = self.conn.getresponse()
		
		# detect the http error codes - if there was an error it was probably the api key
		if r.status is 403:
			raise(Exception('Api key was rejected. Did you paste it in config.json?'))
		elif r.status is not 200:
			raise(Exception('Error making request to nyt.com.'))
		
		return r.read().decode("ascii")


	def get_headline_list(self, *args):
		
	##	  -Function which returns a list comprised of all the headlines in list form 
	##	   of an archive(from a given year, month)

		d = self.get_archive(*args)

		headlineList = []

		for doc in d['response']['docs']:
			if doc['headline']['main'][:5] == 'Front':
				pass
			elif doc['headline']['main'][:7] == 'Article':
				pass
			else:
				headlineList.append(word_tokenize(doc['headline']['main']))
		
		return headlineList


	def get_year_headline_list(self, year = 1853):
		
	##	  -Function which returns a list comprised of all of the headline
                ##               lists of the archives from a given year.

		yearHeadlineList = []

		for month in range(1, 13):
			yearHeadlineList.append(self.get_headline_list(year, month))

		return yearHeadlineList


	def get_year_range_headline_list(self, startYear = 1853, endYear = 1862):
		
	##	  -Function which returns a list comprised of all of the year headline lists 
	##	   of the archives from a given range of years.
		
		yearRangeHeadlineList = []
		
		for year in range(startYear, endYear + 1):
			yearRangeHeadlineList.append(self.get_year_headline_list(year))

		return yearRangeHeadlineList


	def get_time_period_headline_list(self, startYear = 1990, endYear = 1999, \
		  startMonth = 1, endMonth = 12):

	##	  -Function which returns a list comprised of all of the year headline lists 
	##	   of the archives from a given range of years, starting and ending at specific
                ##               months.

		print("Compiling List of NYT headline Year Lists from " + str(startMonth) + ", " \
		  + str(startYear) + " to " + str(endMonth) + ", " + str(endYear) + "...")

		timePeriodHeadlineList = []
		beginYearList = []
		endYearList = []

		for month in range(startMonth, 13):
			beginYearList.append(self.get_headline_list(startYear, month))
		timePeriodHeadlineList.append(beginYearList)
		
		for yearList in self.get_year_range_headline_list(startYear + 1, endYear - 1):
			timePeriodHeadlineList.append(yearList)
	
		for month in range(1, endMonth + 1):
			endYearList.append(self.get_headline_list(endYear, month))
		timePeriodHeadlineList.append(endYearList)

		return timePeriodHeadlineList
	

if __name__ == "__main__":
	import sys

	if len(sys.argv) > 1:
		yr = str(sys.argv[1])
		mo = str(sys.argv[2])
	else:
		yr = 1853
		mo = 12

	# initiate nytapi library
	nytapi = NYT()

	# make a request to get the archive
	d = nytapi.get_archive(year=yr, month=mo)

	
	i = 1
	for doc in d['response']['docs']:
		print(doc['headline']['main'])
		if i > 10:
			break
		i += 1

