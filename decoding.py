import chardet

filename = 'text/book3.txt'

with open(filename, 'rb') as f:
    rawdata = f.read()
    result = chardet.detect(rawdata)
    encoding = result['encoding']

print(f'The encoding of the file is: {encoding}')