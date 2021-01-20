testList = [3, 4, 2, 4, 5, 5, 3, 7, 8, 9, 11, 45, 6, 5]
seenList = []

for test in testList:
    beenSeen = False
    for seen in seenList:
        if (test == seen):
            beenSeen = True
    if not beenSeen:
        seenList.append(test)

print (seenList)