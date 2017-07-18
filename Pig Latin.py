rawInput = raw_input("Word to Pig-Latinify: ")

def piglatinify(input):
    if len(input) > 2:
        for x1 in xrange(len(input)):
            if input[x1] in ('aeiou'):
                firstVowelPosition = x1
                firstVowel = input[x1]
                break

        newWord = input.split(firstVowel, 1)
        pigLatin = firstVowel+newWord[1]+newWord[0]


        if firstVowelPosition != 0: #non first-vowel word
            return pigLatin+"ay"
        else: #first-vowel word
            return pigLatin+"way"
    else:
        return input

finalResult = ""
for x in rawInput.split():
    finalResult += piglatinify(x) + " "
print finalResult

#It doesn't really work when there's two letter words with the vowel at the end
#I've made an exception. Maybe fix some other day?