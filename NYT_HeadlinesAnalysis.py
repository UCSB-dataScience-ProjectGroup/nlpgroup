
## Python Script which accesses the New York Times API and compiles all of the NYT Article Headlines from a given time period. 
## We plan to use the headline data to create wordClouds for each decade from the 1850's to 2000's.


    ## PART 1: Importing Libraries

## Here are the libraries we used:

from nyt import *
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt

## Here are the descriptions of the imported libraries in order.

## 1. (This is a .py script written by Devin which accesses the NYT's API for us.)
## 2. This is the Natural Language Toolkit. We use many of their tools to clean up our raw NYT Headline Data
## 3. Removing stopwords such as "a", "the", "of", etc. allow our analysis to focus on important words
## 4. Allows us to create WordClouds using our Headling String
## 5. Allows us to create visualizations of our WordClouds


    ## PART 2: Creating Functions which grab the data from NYTs and Return Strings

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
                        headlineString += doc['headline']['main'] + ' '

        return headlineString.lower()
    
    
def createYearHeadlineString(year = 1853):
    
##      -Function which returns a string comprised of all of the headlines of the archives from
##       a given year.

        yearHeadlineString = ""

        for month in range(1, 13):
                yearHeadlineString += " " + createHeadlineString(year, month) + ' '

        return yearHeadlineString
    
    
def createYearRangeHeadlineString(startYear = 1853, endYear = 1862):
    
##      -Function which returns a string comprised of all of the headlines of the archives from
##       a given range of years.

        print("Compiling Headling String of NTY headlines from " + str(startYear) + " to " \
                  + str(endYear) + "...")
        
        yearRangeHeadlineString = ""
        
        for year in range(startYear, endYear + 1):
                yearRangeHeadlineString += " " + createYearHeadlineString(year) + ' '

        return yearRangeHeadlineString
    

    ## PART 3: Tokenizing and cleaning up our Strings
    
## What is Tokenization? 
## "Tokenization is the act of breaking up a sequence of strings into pieces such as words, 
##  keywords, phrases, symbols and other elements called tokens."

def tokenizeAndRemoveStopwords(string = createHeadlineString(1865,1)):

##      -Function which tokenizes a string and removes stopwords/punctuation from the list of tokens.
##       This function returns a list of tokens.

        print("Tokenizing and Removing Stopwords...")

        tokens = nltk.word_tokenize(string)
        cleanTokens = []
        cachedStopwords = stopwords.words('english')
        punct = ["'", '.', ',', '-', '--', '?', '!', ':', ';', "'s", '$', '"']
        fluff = cachedStopwords + punct
        
        for token in tokens:
                if token not in fluff:
                        cleanTokens.append(token)
                        
        return cleanTokens
    
    
    ## PART 4: Creating WordClouds from our Tokens :) 
    
def displayWordCloud(tokens = tokenizeAndRemoveStopwords()):
    
##      -Function which takes a list of tokens, and creates a visualization using MatPlotLib
##       and WordCloud

        print("Creating Word Cloud...")
   
        wordcloud = WordCloud().generate(" ".join(tokens))
        plt.imshow(wordcloud)
        plt.axis("off")
    
        plt.show()
    
    
    ## PART 5: Analyzing Decades by visualizing their most Popular Words
    
def returnYearRangeWordCloud(startYear = 1990, endYear = 1999):
    
##      -Function which takes all the NYT headlines from a given range of years,
##       and displays a WordCloud comprised of the time period's most popular words.
##       *This function utilizes all of our previous functions

        yearRangeString = createYearRangeHeadlineString(startYear, endYear)
        yearRangeTokens = tokenizeAndRemoveStopwords(yearRangeString)
    
        displayWordCloud(yearRangeTokens)
    

