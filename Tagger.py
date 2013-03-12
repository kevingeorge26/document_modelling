'''
Created on Feb 20, 2013

@author: kevin
'''

import nltk
from nltk.tag.simplify import simplify_wsj_tag

def print_preposition():
    tokens =  nltk.word_tokenize(" The men are spending an evening in J.'s room, smoking and discussing illnesses they fancy they suffer from.")
    print nltk.pos_tag(tokens)

   


if __name__ == '__main__':
    print "executing"
    print_preposition()
    pass