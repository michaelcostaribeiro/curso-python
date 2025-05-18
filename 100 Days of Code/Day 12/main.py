from art import logo
from random import randint

def game(attempts):
    correctNumber = randint(1,100)
    while attempts != 0:
        print(f'Você tem: {attempts} restantes para tentar adivinhar um número.')
        guess = int(input('Faça uma tentativa: '))
        if(correctNumber == guess): return True
        if(guess-correctNumber>0 and guess-correctNumber<10):
            print('Quase lá, tá um pouco acima')
        elif(guess-correctNumber<0 and guess-correctNumber>-10):
            print('Quase lá, tá um pouco abaixo')
        elif(correctNumber>guess):
            print('Baixo demais!')
        elif(correctNumber<guess):
            print('Alto demais!')
        else:
            print('Input inválido!')
        attempts -= 1
    if attempts == 0: return False


def gameStart():
    print(logo)
    print('Bem vindo ao advinhe o número!')
    choice = input('Escolha uma dificuldade. Digite "facil" ou "dificil": ').lower()
    if choice == 'facil':
        return game(20)
    elif choice == 'dificil':
        return game(5)
    else:
        print('Digite uma dificuldade válida!')
    return None

print('Você ganhou, parabéns!') if gameStart() else print('Você perdeu, que pena!')


