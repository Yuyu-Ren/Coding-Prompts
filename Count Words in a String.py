text = open("textFile.txt").read()


def counter(textFile):
    wordCount = 0
    for words in text.split():
        wordCount = wordCount+1
    return wordCount
print counter(text)
