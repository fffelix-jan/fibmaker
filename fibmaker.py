# Fill in the Blank Maker
# Copyright (c) 2019 Félix An
# MIT License: https://opensource.org/licenses/MIT
# 
# this basically turns all letters a-z and A-Z into underscores. Doesn't work for accented letters tho (sorry Québec)

# SETTINGS:
# If you want to keep words under two blanks there, set this to True. If not, set it to False.
keepShortWords = True


# do not touch anything below this line

# import the string module used by the makeBlank function
import string

# collect input then toss it in a list
print("Type in whatever you want below, press ENTER, and the words will become blanks:")
inStr = input()
wordList = inStr.split(" ")

# function that replaces letters a-z and A-Z with underscores
def makeBlank(mainString):
    for elem in list(string.ascii_lowercase) + list(string.ascii_uppercase):
        if elem in mainString:
            mainString = mainString.replace(elem, "_")
    return mainString


# spit out what you need
for curWord in range(len(wordList)):
    if keepShortWords == True:
        if len(wordList[curWord]) > 2:
            print(makeBlank(wordList[curWord]), end = " ")
        else:
            print(wordList[curWord], end = " ")
    else:
        print(makeBlank(wordList[curWord]), end = " ")