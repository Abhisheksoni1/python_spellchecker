# python_spellchecker

Create a new module named spellchecker.py which when is ran like a script in the terminal takes two argument -> a dictionary and a text file (both given to you).
The module checks spell errors in the text file by comparing it with the words in the dictionary file.
The module should implement the following three functions: 

A) load :
load the dictionary file 
load the text file (to be checked)

B) collect :
create a list of tuples with each tuple containing -> first term as the word and second as its count in the text file( duplicates are not allowed)
and return it 
Arrange the tuples in the decreasing order of the count and in case of tie arrange in the order of the first alphabet of the word, then in the order of second alphabet and so on... 

Ex: if text file is: "betty bought a bit of butter but the butter was bitter"
then collect returns: [('butter', 2), ('a', 1), ('betty', 1), ('bit', 1), ('bitter', 1), ('bought', 1), ('but', 1), ('of', 1), ('the', 1), ('was', 1)] 

also calulate the time taken by this function to exceute and display it.

C) check :
check the list returned by the collect function against the dictionary keeping the given facts in mind

1) case insensitivity(spelling does not deoend on the case of the word)

then finally, display a list of all the mispelled words in the text file
