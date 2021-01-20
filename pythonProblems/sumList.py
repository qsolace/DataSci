intInput = [38, 3, 5, 2, 5, 2,1, 1, 1, 1, 3,4 ,5]

digits = [int(x) for x in intInput]

print (digits)

output = 0

for x in digits:
    output = output + x

print (output)