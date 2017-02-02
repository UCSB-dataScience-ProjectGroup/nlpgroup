

## Connecting to NY Times API

import http.client
import json

conn = http.client.HTTPConnection('api.nytimes.com', 80)
conn.request("GET", "/svc/archive/v1/1851/12.json?api-key=49b5f91ad3b049c2974dc4b5c95be8c1")
r1 = conn.getresponse()
print(r1.status, r1.reason)

d = json.loads(r1.read().decode("ascii"))

##for doc in d['response']['docs']:
##    print(doc['headline']['main'])
    



