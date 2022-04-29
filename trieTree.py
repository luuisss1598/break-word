from difflib import restore
import queue
from collections import deque
from re import search
import string


class trieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Trie:
    def __init__(self):
        self.root = trieNode()

    def insert(self, word):
        # initlize the word at the root
        curr = self.root

        '''
            we are checking for 2 conditions:
                1. if this character does not exist, then it means is not in our hashmap yet, so we have to add it
                2. if this character does exist, then we just add it
        '''

        for i in word:
            if i not in curr.children:
                curr.children[i] = trieNode()
            curr = curr.children[i]

        curr.endOfWord = True

    def search(self, word):
        # we start at the root
        curr = self.root

        for i in word:
            if i not in curr.children:
                return False
            curr = curr.children[i]

        return curr.endOfWord  # return true if the word is in the trie, false if not
    
    def startsWith(self, word):
        # we start at the root
        curr = self.root

        for i in word:
            if i not in curr.children:
                return False
            curr = curr.children[i]

        return True
    
    def getHeightOfWord(self, word):
        curr = self.root
        count = 0
        
        for i in word:
            if i not in curr.children:
                return False
            curr = curr.children[i]
            count += 1
            
        return count

            

