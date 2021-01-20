wordInput = input("Gimme ur werds > ")

wordInput = wordInput.split()

wordDict = dict((k, 1) for k in wordInput)

for word in range(len(wordInput)):
    beenSeen = False
    for seen in range(word):
        if (wordInput[word] == wordInput[seen]):
            beenSeen = True
    if beenSeen:
        wordDict[wordInput[word]] = wordDict[wordInput[word]] + 1

print (len(wordDict))
print (wordDict)