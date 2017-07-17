inputCount = raw_input("String to count number of vowels: ")
vowelTally = vowelSum = 0
for x in xrange(len(inputCount)):
    if inputCount[x] in 'aeiou':
        vowelTally = vowelTally + 1 #counts vowels
        vowelSum = vowelSum + x+1

print "Number of vowels: " + str(vowelTally) + '\n' + "Sum of vowel positions: " + str(vowelSum) #returns number of vowels
