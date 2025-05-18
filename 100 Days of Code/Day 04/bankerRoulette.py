import random


friends = ['Alice', "Bob", "Charlie", "David", "Emanuel"]
randomNumber = random.randint(1,5)-1
rouletteTarget = friends[randomNumber]
print(f'{randomNumber} {rouletteTarget}')


