#hangman
import random
import hangman_art
import hangman_words

def startTheGame(wordToChange,correctWord):
    gameOver = False
    life = 6
    while not gameOver:
        print(hangman_art.stages[life])
        print("".join(wordToChange))
        correctGuess = guessALetter(wordToChange,correctWord)
        if (not correctGuess):
            life -= 1
            print(f'Você tem {life} vidas restantes!')
            if(life == 0):
                print('Que pena, você perdeu!')
                print('GAME OVER')
                gameOver = True
        if(wordToChange == list(correctWord)):
            print(f'A palavra correta é : {correctWord}!')
            print('Você ganhou a forca e salvou nosso amigo hangman, obrigado por jogar!')
            gameOver = True
        
def guessALetter(wordToChange,correctWord):
    guessedLetter = input('Escolha uma letra: ').lower()
    indexesToReplace = letterCheck(guessedLetter)
    if(indexesToReplace):
        print('Você acertou!')
        for i in range(0,len(indexesToReplace)):
            wordToChange[indexesToReplace[i]] = correctWord[indexesToReplace[i]]
        return True
    else:
        print('Você errou!')
        return False

def letterCheck(triedInput):
    checkedCharacters = []
    randomWordAsAList = list(randomWord)
    for i in range(0,len(randomWordAsAList)):
        if randomWordAsAList[i].lower() == triedInput:
            checkedCharacters.append(i)
    if(len(checkedCharacters)>=1):
        return checkedCharacters
    else:
        return False

def generateBlank(word):
    wordAsAList = list(word)
    for i in range(0,len(wordAsAList)):
        wordAsAList[i] = '_'
    return wordAsAList

randomWordsList = ['Perceive','Apple','Slab','Remind','Fool','Display']
randomWord = random.choice(hangman_words.word_list)
wordInBlanks = generateBlank(randomWord)

print(randomWord)
startTheGame(wordInBlanks, randomWord)

