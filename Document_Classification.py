'''
Created on Feb 20, 2013

@author: kevin
'''
import nltk
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from Basic_PreProcessing import get_files
from collections import defaultdict

total_freq = {} # stores the word count for all the docunments
top_counts = [] # stores the top count for the words in the test case
top_count_number = 20 # stores the number of top count you want to use fopr the feature set


freq_file_list = []

classifier = None   

""" add the frequency found in various case"""
def count(line):   
    val = line.strip().split(" ")
    total_freq[ val[1] ] += int( val[0] )    

"""
output folder contains the files that have the frequency count for the test set
 """
def feature_creator():
    global top_counts
    map(lambda y: count(y) ,[ y for x in freq_file_list for y in open(x).readlines() ])    
    top_counts =  sorted(total_freq, key=total_freq.get, reverse=True)[:top_count_number]
    


"""file name is the complete filename 
it should be of the format 
Frequency_of_word Word 

"""
def document_feature(filename):
   
    document_words = set( x.strip().split(" ")[1] for x in open(filename).readlines() )
    features = {}
    for word in top_counts:
        features['contains(%s)' % word] = (word in document_words)
    return features
    
def train_data():
    global classifier
    test_data = [ (document_feature(x), x.split("-")[0] ) for x in freq_file_list ]    
    classifier = nltk.NaiveBayesClassifier.train(test_data)

def classification_init():
    global total_freq,freq_file_list
    
    temp_file =  get_files("./output")
    freq_file_list =  filter( lambda x : x.find("Frequency") >-1 and x.find("classify_data") == -1, temp_file )    
    total_freq = defaultdict(lambda : 0 )
    feature_creator()        

def classify(filenames):
    
    for f in filenames:
        print f
        print classifier.classify(document_feature(f)) 

if __name__ == '__main__':
   
    global classifier
    classification_init()
    train_data()
    
    classify(filter( lambda x : x.find("Frequency") >-1 , get_files("./output/classify_data")))
    
    
   
   
    pass