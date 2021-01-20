creditCardNumber = (input("Credit Card Number > "))#gets an input of the credit card number
creditCardNumber = int(creditCardNumber.replace(" ",""))#remove any whitespace
print(creditCardNumber)

digits = [int(x) for x in str(creditCardNumber)] # makes the input into an array of individual characters

checksum = 0

 # this is the calculations for the checksum
for x in range(len(digits)):
    if (x % 2 == 1):
        continue
    number = digits[x] * 2
    if number >= 10:
        number = 1 + number % 10
    checksum = checksum + number

for x in range(len(digits)):
    if (x % 2 == 0):
        continue
    checksum = checksum + digits[x]

if checksum % 10 != 0:
    print("INVALID")
    exit()

#this is where the individual card distributors are determined (assuming it passes the check sum)

if (len(digits) == 15 and digits[0] == 3 and (digits[1] == 4 or digits[1] == 7)):
    print("AMERICAN EXPRESS")
elif (len(digits) == 16 and digits[0]==5 and (digits[1]<=5 and digits[1]>0)):
    print("MASTERCARD")
elif ((len(digits) == 13 or len(digits) == 16) and digits[0] == 4):
    print("VISA")
elif (len(digits) == 16 and digits[0]==6):
    print("DISCOVER")
else:
    print("INVALID")