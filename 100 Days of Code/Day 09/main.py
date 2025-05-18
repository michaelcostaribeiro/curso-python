from contextlib import nullcontext
import os
import art
print(art.logo)
finished = False

bidList = {}

while not finished:
    name = input('Digite um nome: ')
    os.system('cls')
    bid = float(input("Digite um valor de oferta: R$"))
    bidList[name] = bid
    wannaContinue = input('Tem mais algum ofertador?(S ou N)\n').lower()
    if wannaContinue == 'n':
        finished = True
    elif wannaContinue != 's':
        print('Input Inválido!')
        finished = True

higgestBidder = ''
currentBid = 0
for bid in bidList:
    if(bidList[bid]>currentBid):
        currentBid = bidList[bid]
        higgestBidder = bid

print(f'O vencedor é: {higgestBidder}, com o valor de: {bidList[higgestBidder]}!')



