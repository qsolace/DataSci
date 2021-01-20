inputString = input("String > ")
inputArray = [str(x) for x in str(inputString)]

print (inputArray)

myDict = {i:inputArray.count(i) for i in inputArray}

print (myDict)

keyList = [str(x) for x in myDict.keys()]
print (keyList)
largestValue = ''
secondValue = ''
thirdValue = ''

if (len(keyList)>=1):
    largestValue=keyList[0]
if (len(keyList)>=2):
    if (myDict.get(largestValue) > myDict.get(keyList[1])):
        secondValue = keyList[1]
    else:
        secondValue = largestValue
        largestValue = keyList[1]
if (len(keyList)>=3):
    testKey = myDict.get(keyList[2])
    if (testKey > myDict.get(largestValue)):
        thirdValue = secondValue
        secondValue = largestValue
        largestValue = keyList[2]
    elif(testKey > myDict.get(secondValue)):
        thirdValue = secondValue
        secondValue = keyList[2]
    else:
        thirdValue = keyList[2]
        

for i in keyList:
    testKey = myDict.get(i) 

    if (testKey > myDict.get(largestValue)):
        thirdValue = secondValue
        secondValue = largestValue
        largestValue = i
    elif(testKey > myDict.get(secondValue)):
        thirdValue = secondValue
        secondValue = i
    elif (testKey > myDict.get(thirdValue)):
        thirdValue = i



print ("Largest: ", end="")
print (str(largestValue) + " " + str(myDict.get(largestValue)))

print ("Second: ", end="")
print (str(secondValue) + " " + str(myDict.get(secondValue)))

print ("Third: ", end="")
print (str(thirdValue) + " " + str(myDict.get(thirdValue)))