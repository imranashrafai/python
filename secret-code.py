print("======================== Secret Code Exercise ========================")
# coding
userWord = input("Enter value to encrypt: ")
chars = len(userWord)
randomStart = "yeto"
randomEnd = "hoga"
newSt = ""

if chars > 5:
    newSt = randomStart + userWord + randomEnd
    print("Encoded Text is: ", newSt)

else:
    # to reverse a string [::-1]
    newSt = userWord[::-1]
    print("Encoded Text is: ", newSt)


# decoding
if chars <= 5:
    print("Decoded Text is: ", newSt[::-1])
else:
    decodedDt = newSt[len(randomStart) : len(newSt) - len(randomEnd)]
    print("Decoded Text is: ", decodedDt)
