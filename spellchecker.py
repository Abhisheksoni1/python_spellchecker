import re
import time
from collections import Counter
start_time = 0
def spellcheck(inputfile):
    count = 0 
    filebeingchecked = open(inputfile, 'r')
    spellcheckfile = open("dictionary", 'r')

    dictionary = (spellcheckfile.read().split("\n"))
    words = filebeingchecked.read().lower()

 
    words1 = re.sub("[a-z]*\d[a-z]*"," ",words)
    word1 = re.findall("[a-z]+\'*[a-z]*\'*[a-z]*", words1)
    word_set = Counter(word1)
    distinct_mis_word =set(word1).difference(set(dictionary))
    #for word in distinct_mis_word:
    for word in word_set:

        low = 0
        high=len(dictionary)-1

        while low <= high:

            mid=(low+high)//2
            item=dictionary[mid]

            if word == item:
                break

            elif word < item:
                high=mid-1

            else:
                low=mid+1
        else:
	    count += word_set[word]
            #yield word
        #count += word_set[word]
    print count 
    #print "total word count in text file is "+ str(len(word1))

def main():

    print("This program accepts a file as an input file and uses a spell check function to 
    \nidentify any problematic words that are not found in a common dictionary.")

    inputfile = raw_input("Enter the name of the desired .txt file you wish to spellcheck: ")
    global start_time
    start_time = time.time()

    spellcheck(inputfile)
    
main()

#collect("text.txt")
print("--- %s seconds ---" % (time.time() - start_time))
