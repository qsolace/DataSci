stringList = ["lala", "p", "percy", "luca", "perry", "bob", "kulik", "klasher brak", "python why"]
outputNumber = 0

for name in range(len(stringList)):
    if(len(stringList[name])<2):
        continue
    for index in range(len(stringList) - name):
        if (len(stringList[index + name]) >= 2 and stringList[index + name] != stringList[name]):
            if (stringList[name][0] == stringList[index + name][0] and stringList[name][len(stringList[name])-1] == stringList[index + name][len(stringList[name + index])-1]):
                print (stringList[name] + " " + stringList[name+index])
                outputNumber = outputNumber + 1

print (outputNumber)