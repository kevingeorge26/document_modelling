'''
Created on Feb 20, 2013

@author: kevin
'''

from nltk.corpus import brown
from nltk.corpus import names, stopwords, words

def print_preposition():
    print brown.tagged_words(simplify_tags=True)
    print stopwords


if __name__ == '__main__':
    print_preposition()
    pass