
## Text Analysis with tf-idf
## Analyzing NYTime's Titles


from nyt import *

##if __name__ == "__main__":
##	nytapi = NYT()
##
##	d = nytapi.get_archive(year=1853, month=12)
##
##	for doc in d['response']['docs']:
##		print(doc['headline']['main'])


def createHeadlineString(year = 1853, month = 12):
##      -Function which returns a string comprised of all the headlines of an archive(from a
##       given year, month)
        nytapi = NYT()
        d = nytapi.get_archive(year, month)

        headlineString = ""

        for doc in d['response']['docs']:
                if doc['headline']['main'][:5] == 'Front':
                        pass
                elif doc['headline']['main'][:7] == 'Article':
                        pass
                else:
                        headlineString += doc['headline']['main']

        return headlineString

##Understand TF IDF
##Create Title Strings from entire decade.

def createYearHeadlineString(year = 1853):
##      -Function which returns a string comprised of all of the headlines of the archives from
##       a given year.
        yearHeadlineString = ""

        for month in range(1, 13):
                yearHeadlineString += " " + createHeadlineString(year, month)

        return yearHeadlineString


def createYearRangeHeadlineString(startYear = 1853, endYear = 1862):
##      -Function which returns a string comprised of all of the headlines of the archives from
##       a given range of years.
        
        yearRangeHeadlineString = ""
        
        for year in range(startYear, endYear + 1):
                yearRangeHeadlineString += " " + createYearHeadlineString(year)

        return yearRangeHeadlineString




