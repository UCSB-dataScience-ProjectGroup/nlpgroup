import http.client
import json




class NYT:

	def __init__(self):
		self.conn = http.client.HTTPConnection("api.nytimes.com")
		try:
			with open('config.json','r') as f: #is config.txt a file that needs to be downloaded?
				self.cfg = json.load(f)
		except:
			raise(Exception('Error loading config.json file. Does it exist and is it json?'))

	def get_archive(self, year=1851, month=12):
		''' Either gets previously retreived data or makes a new
		request to the nyt api to get archive data for a given 
		year and month.
		'''

		## for now, this downloads new data every time

		## in the future, store results in a file and if the data
		## 	is requested again then just use the stored data. It
		##  would be reasonable to make a new file for each 
		##  year/month combination.
		json_string = self.archives_api_request(year,month)
		return json.loads(json_string)


	def archives_api_request(self, year, month):
		
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
	

if __name__ == "__main__":
	nytapi = NYT()

	d = nytapi.get_archive(year=1853, month=12)

	print(d)
	for doc in d['response']['docs']:
		print(doc['headline']['main'])
