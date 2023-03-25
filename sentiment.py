import urllib.request
import string 
import re 
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

url = 'https://www.gutenberg.org/cache/epub/1155/pg1155.txt'
with urllib.request.urlopen(url) as f:
    book1 = f.read().decode('utf-8')

f = open('text/Book2.txt', 'r', encoding='utf-8-sig')
book2 = f.read()

f = open('text/Book3.txt', 'r', encoding='utf-8-sig')
book3 = f.read()


"""Analyze the sentiment of the the three books."""

#use the sentiment analyzer
sid = SentimentIntensityAnalyzer()

 #book1
print("Sentiment Analysis of Book1:")
print(sid.polarity_scores(book1))


 #book2
print("Sentiment Analysis of Book2:")
print(sid.polarity_scores(book2))


 #book3
print("Sentiment Analysis of Book3:")
print(sid.polarity_scores(book3))