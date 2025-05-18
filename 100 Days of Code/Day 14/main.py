from game_data import data
from random import randint
import art

DATA_LENGTH = len(data) - 1
current_random_index = randint(0,DATA_LENGTH)
score = 0
print(art.logo)

def format_data(account):
    return f'{account['name']}, a {account['description']}, from {account['country']}'

def check_answer(firstPick, secondPick):
    global score
    if (firstPick or secondPick):
        score += 1
        print('\n' * 100)
        print(art.logo)
        print(f"You're right! Current score: {score}.")
        return True
    else:
        print('\n' * 100)
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
    return False

def comparison():
    global current_random_index
    first_random_index = current_random_index
    current_random_index = randint(0,DATA_LENGTH)
    print(f'Compare A: {format_data(data[first_random_index])}.')
    print(art.vs)
    print(f'Against B: {format_data(data[current_random_index])}.')
    pick = input('Who has more followers? Type "A" or "B":  ').upper()
    pick_A = pick == 'A' and data[first_random_index]['follower_count']>data[current_random_index]['follower_count']
    pick_B = pick == 'B' and data[current_random_index]['follower_count']>data[first_random_index]['follower_count']
    return comparison() if check_answer(pick_A,pick_B) else False

comparison()