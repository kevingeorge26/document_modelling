#!/usr/bin/env python

'''
Created on Jan 28, 2013

@author: kevin
'''
from string import maketrans
from string import punctuation
from collections import defaultdict
import nltk
from nltk.collocations import *
import sys
import os
from os import listdir,walk
from os.path import isfile, join

final_list = {}


def get_rfc_text():
    """ write the code to get the rfc text """
    pass


def calculate_word_freq(filename,number_of_words):
    
    
    """ code to get the word count in the protocol """
    """ prints the top number_of_words"""
    
    
    with open(filename) as f:
        for i in f:
            with_stop_words = i.strip().translate(trantab).lower()
            without_stop_words = filter(lambda x: x not in stop_words, with_stop_words.split())
            
            for word in without_stop_words:
                final_list[word]+=1
        
    output = open( filename.replace("input","output").replace( ".txt" ," _Frequency.txt"), "w")    
    
    
    counter = 0            
    for words in sorted(final_list, key=final_list.get, reverse=True):
        output.write( " {0} {1} \n" .format(final_list[words], words) )
        
        
        if counter > number_of_words:
            break        
        counter+=1
                

def calculate_bigrams(filename,number_bigrams):
    """ print top number_bigrams bigrams """
    bigram_measures = nltk.collocations.BigramAssocMeasures()
    finder = BigramCollocationFinder.from_words(open(filename).read().split())
    scored = finder.score_ngrams( bigram_measures.likelihood_ratio  )
    scored.sort(key = lambda x:x[1],reverse=True)
    
    output = open(filename.replace("input","output").replace( ".txt" ," _BiGrams.txt"),"w")    
    output.write("\n".join( "%s %s" %x for x in scored[:number_bigrams] ) )
    
        
def get_files(path_name):
    f = []
    for (dirpath, dirname, filenames) in walk(path_name):
        f.extend(map(lambda x: dirpath+"/" +x ,filenames))
   
    return f



if __name__ == '__main__':
    

    global final_list
    
    if( len(sys.argv) >1 ):
        if len(sys.argv) == 3:
            
            number_of_words = sys.argv[1]
            number_bigrams = sys.argv[2]
            
        else:
            print "the usage is python Basic_PreProcessing <number of frequency count> < number of bigrams>"
            print "Going to use the default values"
           
            number_of_words = 200
            number_bigrams = 200
            
       
    else:
        
        number_of_words = 200
        number_bigrams = 200
    
   
    final_list = defaultdict(lambda: 0)
    
    trantab = maketrans(punctuation, " " * len(punctuation))
    stop_words  = set(line.strip() for line in open("stop_words.txt") )
          
    for filename in get_files("./input"):
        final_list.clear()
        calculate_word_freq(filename,int(number_of_words) )
        calculate_bigrams(filename,int(number_bigrams) )    
    
    pass