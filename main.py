import nltk
import re

f = open('Sample.c', 'r')
a = f.read()
count = 0

# Tokens = [] #

Keywords = "int|float|bool|function|void|char|string|array|return|while|if|else|break"
Operators = "(\*)|(\++)|(-)|(=)|(\*)|(\**)|(/)|(%)|(--)|(<)|(>)|(==)|(!=)|(||)|(&&)"
SpecialChar = "!#|{}():;,.']{}"
Identifiers = "^[a-zA-Z_][a-zA-Z0-9_]*"

dataFlag = False
program = a.split("\n")
for line in program:
    count = count + 1
    print("line No:", count, "\n", line)

    tokens = line.split(' ')
    print("The tokens are ", tokens)
    print("line No:", count, "properties \n")
    for token in tokens:
        if re.findall(Keywords, token):
            print(token, " is a Keyword")
        elif re.findall(Operators, token):
            print(token, "is a Operator")
        elif re.findall(SpecialChar, token):
            print(token, "is a Special Character")
        elif re.findall(Identifiers, token):
            print(token, "is a Identifier")

    dataFlag = False
    print(" Error Token unidentified")
