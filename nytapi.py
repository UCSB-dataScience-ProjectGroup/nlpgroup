import http.client
import json




class Nytapi:

	def __init__(self):
		self.conn = http.client.HTTPConnection("api.nytimes.com")

	def req(self, year=1851, month=12):
		self.conn.request("GET", "//svc/archive/v1/" + str(year) + \
		"/" + str(month) + ".json?api-key=")
		r = self.conn.getresponse()
		return json.loads(r.read().decode("ascii"))

#d = json.loads(r.read().decode("ascii"))


if __name__ == "__main__":
	nytapi = Nytapi()

	d = nytapi.req(1851, 12)

	for doc in d['response']['docs']:
		print(doc['headline']['main'])
