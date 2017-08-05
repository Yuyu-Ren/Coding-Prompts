input = raw_input("Count Strings of: ")

inputList = input.split()

wordCount = 0
for x in inputList:
    wordCount = wordCount+1

print wordCount
