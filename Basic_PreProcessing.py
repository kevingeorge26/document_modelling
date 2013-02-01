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


def process_rfc():
    """ code to get the word count in the protocol """
    with open("test.txt") as f:
        for i in f:
            with_stop_words = i.translate(trantab).lower()
            without_stop_words = filter(lambda x: x not in stop_words, with_stop_words.split(" "))
            
            for word in without_stop_words:
                final_list[word]+=1
                
    for words in sorted(final_list, key=final_list.get, reverse=True):
        print final_list[words] , words
                

def calculate_bigrams():
    """ print top 10 bigrams """
    bigram_measures = nltk.collocations.BigramAssocMeasures()
    finder = BigramCollocationFinder.from_words(open("test.txt").read().split())
    print finder.nbest(bigram_measures.pmi, 10)  
        

if __name__ == '__main__':
    
    global final_list
    final_list = defaultdict(lambda: 0)
    
    trantab = maketrans(punctuation, " " * len(punctuation))
    stop_words  = set(open("stop_words.txt").read().split(","))
#    process_rfc()
    calculate_bigrams()
    
   
    
    pass