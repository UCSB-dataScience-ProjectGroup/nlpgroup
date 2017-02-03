import http.client
import json




class NYT:

	def __init__(self):
		self.conn = http.client.HTTPConnection("api.nytimes.com")
		with open('config.txt','r') as f:
			self.cfg = json.load(f)

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
		return self.archives_api_request(year,month)


	def archives_api_request(self, year, month):
		self.conn.request("GET", "//svc/archive/v1/" + str(year) + \
		"/" + str(month) + ".json?api-key=%s" % (self.cfg['apikey'],))
		r = self.conn.getresponse()
		
		if r.status is not 200:
			raise(Exception('Query to NYT failed. Did you insert your api key in config.txt?'))
		
		return json.loads(r.read().decode("ascii"))

#d = json.loads(r.read().decode("ascii"))


if __name__ == "__main__":
	nytapi = NYT()

	d = nytapi.get_archive(year=1851, month=12)

	print(d)
	for doc in d['response']['docs']:
		print(doc['headline']['main'])
