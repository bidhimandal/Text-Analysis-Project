import urllib.request
import string 
import re 
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download the text file from Project Gutenberg

url = 'https://www.gutenberg.org/cache/epub/1155/pg1155.txt'
with urllib.request.urlopen(url) as f:
    book1 = f.read().decode('utf-8')

f = open('text/Book2.txt', 'r', encoding='utf-8-sig')
book2 = f.read()

f = open('text/Book3.txt', 'r', encoding='utf-8-sig')
book3 = f.read()

def word_frequency(text):
    """ This function will help read a file and return the frequency of various words in that file."""
    if not text:
        print("No text found.")
        return

    #remove punctuation and make all words lowercase
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.lower()

    # Split the string into a list of words
    words = re.findall(r'\b\w+\b', text)

    # Remove the stop words
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]

    # Create a dictionary to hold the word counts and count the words
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    #sorting words by frequency
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    # Print the words and their frequencies
    print("Following is the dictionary of words that appear in the Book with their respective frequencies:") 
    for word, count in sorted_words:
        print(word, count)

    #print top 10 words
    print("Following are the top 10 words that appear in the Book with their respective frequencies:")
    for word, count in sorted_words[:10]:
        print(word, count)
word_frequency(book1)

word_frequency(book2)

word_frequency(book3)


