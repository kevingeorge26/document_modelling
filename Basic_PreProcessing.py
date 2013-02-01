'''
Created on Jan 28, 2013

@author: kevin
'''
from string import maketrans
from string import punctuation
from collections import defaultdict
import nltk
from nltk.collocations import *

final_list = {}

def get_rfc_text():
    """ write the code to get the rfc text """
    pass


def calculate_word_freq(filename,number_of_words):
    
    """ code to get the word count in the protocol """
    """ prints the top number_of_words"""
    with open(filename) as f:
        for i in f:
            with_stop_words = i.translate(trantab).lower()
            without_stop_words = filter(lambda x: x not in stop_words, with_stop_words.split(" "))
            
            for word in without_stop_words:
                final_list[word]+=1
    counter = 0            
    for words in sorted(final_list, key=final_list.get, reverse=True):
        print final_list[words] , words
        
        if counter > number_of_words:
            break
        
        counter+=1
                

def calculate_bigrams(filename,number_bigrams):
    """ print top number_bigrams bigrams """
    bigram_measures = nltk.collocations.BigramAssocMeasures()
    finder = BigramCollocationFinder.from_words(open(filename).read().split())
    scored = finder.score_ngrams( bigram_measures.likelihood_ratio  )
    scored.sort(key = lambda x:x[1],reverse=True)
    print scored[:number_bigrams]
        

if __name__ == '__main__':
    
    global final_list
    final_list = defaultdict(lambda: 0)
    
    trantab = maketrans(punctuation, " " * len(punctuation))
    stop_words  = set(open("stop_words.txt").read().split(","))
    
    calculate_word_freq(filename="test.txt",number_of_words = 10)
    calculate_bigrams(filename="test.txt",number_bigrams=10)
    
   
    
    pass