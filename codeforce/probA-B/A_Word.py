word = input()

lowerCount = 0
upperCount = 0

for letter in word:
    if letter >= 'A' and letter <= 'Z':
        upperCount+=1
    else:
        lowerCount+=1

if upperCount > lowerCount:
    print(word.upper())
else:
    print(word.lower())