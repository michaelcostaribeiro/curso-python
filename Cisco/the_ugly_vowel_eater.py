user_word = input("Enter a word")

for letter in user_word:
    if letter.upper() == "A" or letter.upper() == "E" or letter.upper() == "I" or letter.upper() == "O" or letter.upper() == "U" :
        continue
    else:
        print(letter.upper())
