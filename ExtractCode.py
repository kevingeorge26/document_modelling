'''
Created on Apr 3, 2013

@author: kevin


generate frequency of both implementation and protocol
maintain a file in the input folder that maps protocol to implementation 

syntax of the file (assumming there can be many files for the same protocol and implematation)
protocol filename , protocol filename ... ; implementation filename, implementation filename...

'''
from string import maketrans
from string import punctuation


freq_file_location = "./output/data/RFC/"
source_file_location = "./input/data/RFC/"
implementation_details = "./input/implementation_details.txt"


""" 

"""
def get_freq_files():
    
    stop_words  = set(line.strip() for line in open("stop_words.txt") )
    trantab = maketrans(punctuation, " " * len(punctuation))
    
    for line in open(implementation_details):
        protocol = line.split(";")[0].split(",")
        impl     = line.split(";")[1].split(",")
        
        
        unique_keys = set([]) 
       
        
        for protocol_files in protocol:
            for key in open( freq_file_location + protocol_files.replace( ".txt" ,"_Frequency.txt") ):
                unique_keys.add(key.split(" ")[2])
                
        for implementation_files in impl: # for each implementation file
            imp_keys = set([])
            for key in open( freq_file_location + implementation_files.replace( ".txt" ,"_Frequency.txt") ):
                if key.split(" ")[2] in unique_keys:
                    imp_keys.add(key.split(" ")[2] )
            
            print "***************" + str(len(imp_keys)) + "***********"
            print imp_keys
            
            counter = 0        
            for lines in open( source_file_location + implementation_files ):
                with_stop_words = lines.strip().translate(trantab).lower()
                without_stop_words = filter(lambda x: x not in stop_words, with_stop_words.split())
                
                if len(filter(lambda x : x in imp_keys,without_stop_words) ) >0:
                    counter+=1
                    
            print "total lines " + str(counter)
                    
            
        

        
if __name__ == '__main__':
   
    
    get_freq_files()   

    
    
    
    pass