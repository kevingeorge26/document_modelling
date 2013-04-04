'''
Created on Apr 3, 2013

@author: kevin


generate frequency of both implementation and protocol
maintain a file in the input folder that maps protocol to implementation 

syntax of the file (assumming there can be many files for the same protocol and implematation)
protocol filename , protocol filename ... ; implementation filename, implementation filename...

'''
from os import listdir,walk


freq_file_location = "./output/data/RFC"
source_file_location = "./input/data/RFC"
implementation_details = "./input/implemetation_details.txt"

processed_file = set([])
unprocessed_file = []

""" 
Returns the list of Frequnecy files that are there after Basic_Frequency
"""
def get_freq_files():
    for (dirpath, dirname, filename) in walk(freq_file_location):
        print filename
        unprocessed_file.extend(map(lambda x: dirpath+"/" +x ,filter(lambda x:"imp_Frequency" in x,filename)))

def process_file():
    
    for x in unprocessed_file:
        x.find()
        
        
if __name__ == '__main__':
    
   
    
    get_freq_files()   
    process_file()
    
    
    
    pass