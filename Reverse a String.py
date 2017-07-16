raw_string = raw_input("String to be reversed ")
reversed_string = ""

for x in xrange(len(raw_string)-1, -1, -1):
    reversed_string = reversed_string + raw_string[x]

print reversed_string
