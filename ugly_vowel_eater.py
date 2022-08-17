##
# This programs eats up the vowels in a word and prints the remaining words on independent lines in capital letters.
##

user_word = input("Enter a word:")

user_word = user_word.upper()

for i in user_word:
    if i == "A":
        continue
    elif i == "E":
        continue
    elif i == "I":
        continue
    elif i == "O":
        continue
    elif i == "U":
        continue
    else:
        print(i)
