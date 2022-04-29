from itertools import count
from xml.sax.handler import property_interning_dict
from trieTree import *
from collections import defaultdict
from asyncio import ReadTransport
import re

#use a global variable to return the array of arrays that contains the sentences 
globalArrayOfArrays = []

def restoreSpaces(words, trie, storeSenteces= list()):  
    
    length = len(words)
    
    
    if length == 0:
        global globalArrayOfArrays
        # print(" ".join(i for i in storeSenteces))
        
        globalArrayOfArrays.append(storeSenteces)
        
        # f = open('FinalSentences.txt', 'a')
        # f.write(" ".join(i for i in storeSenteces) + "\n\n")
        # f.close()
        
        return
    
    for i in range(1, length+1):
        if trie.search(words[0:i]):
            sentence = storeSenteces+[words[0:i]]
            restoreSpaces(words[i:], trie, storeSenteces = sentence)
        
        
def getRankingForWords(fileName):
    #store the words into a dictionary and assign a value for each 100 words
    myDictRanking = {}
    
    f = open(fileName, encoding = "ISO-8859-1");
    word = f.read().splitlines()
    counter1 = 0
    value = 1
    for i in word:
        if len(i) > 1:
            if counter1 == 100:
                value += 1;
                counter1 = 0
            if i not in myDictRanking:
                myDictRanking[i] = value
                
            counter1 += 1
            
    f.close()
    
    myDictRanking['I'] = 1;
    myDictRanking['a'] = 1;
    myDictRanking['math'] = 1
    myDictRanking['mp'] = 20
    myDictRanking['.'] = 0
    myDictRanking[','] = 0
    
    return myDictRanking

def getDictionary2(fileName):
    #store the words into set
    mySet = set()
    
    f = open(fileName, encoding = "ISO-8859-1");
    word = f.read().splitlines()
    for i in word:
        if len(i) > 1:
            mySet.add(i);
            
    f.close()
    
    mySet.add('I');
    mySet.add('a');
    mySet.add('math');
    mySet.add('.')
    mySet.add(',')
    # mySet.add('mangoes')
    
    return mySet

def arrayToSentence(arrSentence):
    finalSentence = ''
    for i in arrSentence:
        finalSentence += i + ' ';
        
    return finalSentence

def getSentenceRanking(myDictRanking, arraySentence):
    numberRanking = 0
    arrLength = len(arraySentence)
    
    for i in arraySentence:
        numberRanking += myDictRanking[i];
        
    return (numberRanking/arrLength)

def writeIntoFileAndConsole(textFile, myDictRanking):
    storeRankingSentences = {}
    
    for i in globalArrayOfArrays:
        storeRankingSentences[getSentenceRanking(myDictRanking, i)] = (arrayToSentence(i))
    
    
    print('\nFrom most common to least common: \n\n')
    f = open(textFile, 'a')
    f.write('From most common to least common: \n\n')
    for i in sorted (storeRankingSentences.keys()):
        f.write(re.sub(r'\s([?.,!"](?:\s|$))', r'\1', str(storeRankingSentences.get(i))) + '\n')
        # print(str(storeRankingSentences.get(i)) + "\n")
        print(re.sub(r'\s([?.,!"](?:\s|$))', r'\1', str(storeRankingSentences.get(i))) + '\n')
    f.close()
    


if __name__ == "__main__":  
    '''
        1. First we need to read the words from the dictionary 
        2. Store the letters into a dictionary (hashmap) searching and inserting time complexity O(1)
        3. Output the dictionary, make sure it works
    '''
    
    # get the missing sentence from the messed up file and store it into a string
    f = open('missing3.txt', encoding = "ISO-8859-1");
    word = f.read().splitlines()
    
    getMissingSpaceSentence = ''
    for i in word:
        getMissingSpaceSentence = i
    
    print(getMissingSpaceSentence)
    # store the words into a set
    mySet = set()
    mySet = getDictionary2('dictionary2.txt');
    
    #store the ranking of the words into a dictionary
    myDictRanking = {}
    myDictRanking = getRankingForWords('dictionary.txt')

    # implement the trie tree
    myTrie = Trie();
    
    # insert words into trie tree
    for i in mySet:
        myTrie.insert(i);
    
    restoreSpaces(getMissingSpaceSentence, myTrie)
    writeIntoFileAndConsole('finalSentence3.txt', myDictRanking);

    
    
    
    
    
    
    

    # word = 'welcometomyhomeinwherewelivearoundbigbuildingsandwegotothebigapplewherewemeetotherpeoplethenwegooutfordinnertogetherwithmyfamily'
    # word = "Ilikemathandcomputerscience"
    # word = "ahousethatisinthecorneroftheworld"
    # word = 'Thisclassicstorytellsthestoryofaveryslowturtleandaspeedyrabbit.Theturtlechallengestherabittoarace.Therabitlaughsattheideathataturtlecouldrunfasterthanhimbutwhenthetwoactuallyracetheresultsaresurprising'
    # word = 'Ilikeicecreamandmangoes,butalsoapples.'