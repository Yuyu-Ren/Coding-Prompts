input = raw_input("Word to Pig-Latinify: ")

for x in xrange(len(input)):
    if input[x] in ('aeiou'):
        firstVowelPosition = x
        firstVowel = input[x]
        break

newWord = input.split(firstVowel, 1)
pigLatin = firstVowel+newWord[1]+newWord[0]


if firstVowelPosition != 0: #non first-vowel word
    print pigLatin+"ay"
else: #first-vowel word
    print pigLatin+"way"