input = raw_input("Palindrome Checker: ")
length = len(input)

def checkpalindrome():
    # type: () -> object
    secondCutDecrement = len(splitInput[1]) - 1
    for x in splitInput[0]:
        if x == splitInput[1][secondCutDecrement]:
            secondCutDecrement -= 1
            continue
        else:
            return "Not Palindrome!"

    else:
        return "Palindrome!"


if length % 2 is 0:
    # even-count word length
    length = len(input) / 2  # location of slice
    splitInput = input[:length], input[length:]  # slices input into two pieces
    print checkpalindrome()

else:
    # uneven-count word length
    length = len(input) / 2 # location of slice
    splitInput = input[:length], input[length + 1:]  # slice into two pieces, omitting the middle letter
    print checkpalindrome()
