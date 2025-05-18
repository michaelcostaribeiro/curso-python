from art import logo
import random
blackJackCards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def winCondition(player, enemy):
    if player>enemy and player<22 or enemy>21:
        return True
    elif enemy>player and enemy<22:
        return False
    else:
        return None

def resultRender(condition):
    return 'Você venceu, parabéns!' if condition else f'Você perdeu, que pena!'

def cardSum(handPick):
    sum = 0
    for card in handPick:
        sum = sum + card
    return sum

def playerPick():
    playerHand = [random.choice(blackJackCards),random.choice(blackJackCards)]
    pickMoreCards = True
    while pickMoreCards:
        if(cardSum(playerHand)>21):
            return playerHand
        choice = input(f'Sua mão tem as cartas: {playerHand}, você deseja puxar mais alguma carta? (soma das cartas: {cardSum(playerHand)}) (S/N)').lower()
        if(choice == 's'):
            playerHand.append(random.choice(blackJackCards))
        else:
            return playerHand
    return playerHand


def enemyPick():
    enemyHand = []
    while not cardSum(enemyHand)>17:
        enemyHand.append(random.choice(blackJackCards))
    return enemyHand

def enemyRender(hand):
    renderList = hand[:]
    renderList[0] = '_'
    return f'A mão do inimigo está em: {renderList}'

def gameStart():
    print(logo)
    wannaContinue = True
    while wannaContinue:
        enemy = enemyPick()
        enemySum = cardSum(enemy)
        print(enemyRender(enemy))
        player = playerPick()
        playerSum = cardSum(player)
        print(f'Sua mão é: {playerSum}')
        print(f'A mão do seu inimigo é: {enemySum}')
        if(enemySum == playerSum and enemySum == 21):
            print('Empate')
        else:
            print(resultRender(winCondition(playerSum, enemySum)))
        continuar = input('Você quer continuar?').lower()
        if(continuar == 's'):
            return gameStart()
        else:
            wannaContinue = False
    return None


gameStart()