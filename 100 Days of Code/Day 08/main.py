import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_length = len(alphabet)
def startProgram():
    print(art.logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = symbols_and_numbers_test()
    shift = int(input("Type the shift number:\n"))
    ceasar(direction, text, shift)

    return startProgram()


def symbols_and_numbers_test():
    text = list(input("Type your message:\n").lower())
    for i in text:
        if i not in alphabet:
            print('Please, no symbols nor numbers!')
            return symbols_and_numbers_test()
    return text


def encrypt(original_text, shift_amount):
    encrypted_text = ''
    for i in range(0, len(original_text)):
        currentLetterIndex = alphabet.index(original_text[i])
        indexAfterChange = currentLetterIndex + shift_amount

        indexAfterChange%= len(alphabet)

        if(indexAfterChange<alphabet_length):
            encrypted_text += alphabet[indexAfterChange]
        else:
            encrypted_text +=  alphabet[indexAfterChange-alphabet_length]
    return encrypted_text

def decrypt(original_text, shift_amount):
    decrypted_text = ''
    negative_alphabet_length = alphabet_length*-1
    for i in range(0, len(original_text)):
        currentLetterIndex = alphabet.index(original_text[i])
        indexAfterChange = currentLetterIndex - shift_amount

        if(indexAfterChange<negative_alphabet_length):
            while (indexAfterChange<negative_alphabet_length):
                indexAfterChange+=alphabet_length

        decrypted_text += alphabet[indexAfterChange]
    return decrypted_text

def ceasar(choice, original_text, shift_amount):
    if(choice == 'encode'):
        print(encrypt(original_text, shift_amount))
    elif(choice == 'decode'):
        print(decrypt(original_text,shift_amount))
    else:
        print('invalid input!')

startProgram()


