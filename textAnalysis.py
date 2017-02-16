
## Text Analysis with tf-idf
## Analyzing NYTime's Titles


from nyt import *

if __name__ == "__main__":
	nytapi = NYT()

	d = nytapi.get_archive(year=1853, month=12)

##	for doc in d['response']['docs']:
##		print(doc['headline']['main'])


def createHeadlineString(archive):
##      Function which returns a string comprised of all the headlines of an archive(from a
##      given year, month)
        
        headlineString = ""

        for doc in d['response']['docs']:
                if doc['headline']['main'][:5] == 'Front':
                        pass
                elif doc['headline']['main'][:7] == 'Article':
                        pass
                else:
                        headlineString += doc['headline']['main']

        return headlineString
