
## Text Analysis with tf-idf
## Analyzing NYTime's Titles


from nyt import *
import nltk
from nltk.corpus import stopwords
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

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
                        headlineString += doc['headline']['main'] + ' '

        return headlineString.lower()

##Understand TF IDF
##Create Title Strings from entire decade.

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
        
        yearRangeHeadlineString = ""
        
        for year in range(startYear, endYear + 1):
                yearRangeHeadlineString += " " + createYearHeadlineString(year) + ' '

        return yearRangeHeadlineString


def removeStopwords(tokens):
##      -Function which removes stopwords from a list of tokens.
        cleanTokens = []
        for token in tokens:
                if token not in stopwords.words('english') and \
                   token not in ["'", '.', ',', '-', '--', '?', '!', ':', ';', "'s", '$', '"']:
                        cleanTokens.append(token)
        return cleanTokens


g = createHeadlineString(1865, 1)
## Creates String of Headlines from NYT articles in Jan 1865
gt = nltk.word_tokenize(g)
## Tokenize a string
gtf = removeStopwords(gt)
## Remove stopwords in a string
gtfo = nltk.Text(gtf)
## Convert a list of tokens to a nltk Text 


count = Counter(gtf)
## Create a dictionary with keys = Words and values = WordCounts

#print(count.most_common(10))
## print the 10 most common words in the tokenized list with their counts


taggedTupleList = nltk.pos_tag(gtfo)
## Pinpoint the part of speech of words in the text gtfo. taggedTupleList returns a list of tuples
## comprised of ('word', 'Part of Speech') i.e. ('rebel', 'NN')


wordcloud = WordCloud().generate(" ".join(gtfo))
#Generate a word cloud image

# Display the generated image:
# the matplotlib way:
plt.imshow(wordcloud)
plt.axis("off")


