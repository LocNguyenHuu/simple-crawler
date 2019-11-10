# Python3 program for a word frequency
# counter after crawling a web-page
import requests
from bs4 import BeautifulSoup
from collections import Counter


'''Defining the web-crawler/core spider, which will fetch information from a given website
, and push contents to a second function clean_wordlist()'''
def start(url):

    # Empty list to store the contents
    wordlist = []
    source_code = requests.get(url).text

    # Ping the request url for data
    soup = BeautifulSoup(source_code, 'html.parser')

    for each_text in soup.findAll('div', {'class': 'entry-content'}):
        content = each_text.text

        # Use split() to break the sentence into words
        words = content.lower().split()

        for earch_word in words:
            wordlist.append(earch_word)

        clean_wordlist(wordlist)

# Function removes any unwanted symbols
def clean_wordlist(wordlist):
    clean_list = []
    for word in wordlist:
        symbols = '!@#$%^&*()_-+={[}]|\;:"<>?/., '

        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')

        if len(word) > 0:
            clean_list.append(word)

    create_dictionary(clean_list)

# Function creates a dictionary containing each word
def create_dictionary(clean_list):
    word_count = {}

    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1


    c = Counter(word_count)
    top = c.most_common(10)
    print(top)

# Driver code
if __name__ == '__main__':
    start("https://www.geeksforgeeks.org/programming-language-choose/")