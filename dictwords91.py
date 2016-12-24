#!/usr/bin/python2
# Exercise 9.1
# Looks up a word in words.txt and returns true using dictionarys

inpWord = raw_input('Word to lookup: ')

fname = open('words.txt')

wordDict = dict()

# old code
#for line in fname:
#    words = line.split()
#    if len(words) == 0: continue
#    for w in words:
#        wordDict[w] = 'whatever'

# new code after watching worked excersie video
text = fname.read()
words = text.split()
for w in words: wordDict[w] = 'whatever'

if inpWord in wordDict:
    print "The word %s is in %s" % (inpWord, "words.txt")
else:
    print "no results found"
