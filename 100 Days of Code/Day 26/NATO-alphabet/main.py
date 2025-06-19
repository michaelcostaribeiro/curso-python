import pandas

nato = pandas.read_csv('nato_phonetic_alphabet.csv')


alphabet_in_nato = {}

for (index, row) in nato.iterrows():
    alphabet_in_nato.update({row.letter:row.code})


word_array = list('test'.upper())

print(f'{word_array} goes like: ')
for letter in word_array:
    if letter in alphabet_in_nato:
        print(alphabet_in_nato[letter])

