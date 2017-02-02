import http.client
import json


conn = http.client.HTTPConnection("api.nytimes.com")
conn.request("GET", "//svc/archive/v1/1851/12.json?api-key=49b5f91ad3b049c2974dc4b5c95be8c1")
r = conn.getresponse()
print(r.status, r.reason)

#print(type(r.read()))

#d = r.read()

#print(d.decode("utf-8"))

#d = json.loads(r.read().decode("ascii"))

d = json.loads(r.read().decode("ascii"))


#print(d.keys())
for doc in d['response']['docs']:
	print(doc['headline']['main'])
