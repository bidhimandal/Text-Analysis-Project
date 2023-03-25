import urllib.request 
import nltk

url = 'https://www.gutenberg.org/cache/epub/1155/pg1155.txt'
with urllib.request.urlopen(url) as f:
    book1 = f.read().decode('utf-8')

f = open('text/Book2.txt', 'r', encoding='utf-8-sig')
book2 = f.read()

f = open('text/Book3.txt', 'r', encoding='utf-8-sig')
book3 = f.read()

#find the number of unique words in each book
unique1 = set(book1.split())
unique2 = set(book2.split())
unique3 = set(book3.split())

print("Number of unique words in Book1: ", len(unique1))
print("Number of unique words in Book2: ", len(unique2))
print("Number of unique words in Book3: ", len(unique3))