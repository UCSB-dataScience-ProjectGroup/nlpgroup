
## Headline List Function - NLP Group
## Jonathan Trinh 4/5/17

## This .py file grabs and organizes Headlines from New York Times articles dating back to 1853.
## The method of organization is as follows:
##
## createTimePeriodHeadlineList will return a list of years: [  [year1] [year2] ....... ]
## within each year is a list of months: [yearX] = [  [month1] [month2] .... ]
## within each month is a list of all headlines in list form: [monthX] = [  [headline1] [headline2] .... ]
## headlineX example: ['Heavy', 'Fighting', 'Erupts', 'in', 'Somali', 'Capital']

from nyt import *
from nltk import word_tokenize

def createHeadlineList(year = 1853, month = 12):
    
##      -Function which returns a list comprised of all the headlines in list form 
##       of an archive(from a given year, month)

        nytapi = NYT()
        d = nytapi.get_archive(year, month)

        headlineList = []

        for doc in d['response']['docs']:
                if doc['headline']['main'][:5] == 'Front':
                        pass
                elif doc['headline']['main'][:7] == 'Article':
                        pass
                else:
                        headlineList.append(word_tokenize(doc['headline']['main']))
                        
        return headlineList


def createYearHeadlineList(year = 1853):
    
##      -Function which returns a list comprised of all of the headline lists of the archives from
##       a given year.

        yearHeadlineList = []

        for month in range(1, 13):
                yearHeadlineList.append(createHeadlineList(year, month))

        return yearHeadlineList


def createYearRangeHeadlineList(startYear = 1853, endYear = 1862):
    
##      -Function which returns a list comprised of all of the year headline lists 
##       of the archives from a given range of years.
        
        yearRangeHeadlineList = []
        
        for year in range(startYear, endYear + 1):
                yearRangeHeadlineList.append(createYearHeadlineList(year))

        return yearRangeHeadlineList


def createTimePeriodHeadlineList(startYear = 1990, endYear = 1999, \
                                                              startMonth = 1, endMonth = 12):

##      -Function which returns a string comprised of all the headlines of the archives from
##       a given time period.

        print("Compiling List of NYT headline Year Lists from " + str(startMonth) + ", " \
                      + str(startYear) + " to " + str(endMonth) + ", " + str(endYear) + "...")

        timePeriodHeadlineList = []
        beginYearList = []
        endYearList = []

        for month in range(startMonth, 13):
                beginYearList.append(createHeadlineList(startYear, month))
        timePeriodHeadlineList.append(beginYearList)
        
        for yearList in createYearRangeHeadlineList(startYear + 1, endYear - 1):
                timePeriodHeadlineList.append(yearList)
                
        for month in range(1, endMonth + 1):
                endYearList.append(createHeadlineList(endYear, month))
        timePeriodHeadlineList.append(endYearList)

        return timePeriodHeadlineList









        
