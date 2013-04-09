'''
Created on Feb 20, 2013

@author: kevin
'''

import nltk
from nltk.tag.simplify import simplify_wsj_tag

def print_preposition():
    print dir(nltk)
    temp = "Or should we make sure the new grammar does not lose other valid English sentences that could have been generated with the original grammar"
    tokens =  nltk.word_tokenize(temp)
#    print nltk.pos_tag(tokens)
    
   

   


if __name__ == '__main__':
    print "executing"
    print_preposition()
    pass