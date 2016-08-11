import re
import time
from collections import Counter
start_time = 0
def spellcheck(inputfile):
    count = 0 
    dictionary = open("dictionary", 'r').split("\n")
    words = open(inputfile, 'r').read().lower()

 
    words1 = re.sub("[a-z]*\d[a-z]*"," ",words)
    word1 = re.findall("[a-z]+\'*[a-z]*\'*[a-z]*", words1)
    word_set = Counter(word1)
    distinct_mis_word =set(word1).difference(set(dictionary))
    for word in distinct_mis_word:
        count += word_set[word]
    print count 
    print "total word count in text file is "+ str(len(word1))

if __name__ == "__main__"
    print("This program accepts a file as an input file and uses a spell check function to
    \nidentify any problematic words that are not found 				in a common dictionary.")
    inputfile = raw_input("Enter the name of the desired .txt file you wish to spellcheck: ")
    global start_time
    start_time = time.time()

    spellcheck(inputfile)
    


#collect("text.txt")
print("--- %s seconds ---" % (time.time() - start_time))
