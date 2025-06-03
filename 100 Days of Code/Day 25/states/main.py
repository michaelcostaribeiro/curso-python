import pandas as p
import turtle as t

STATES_CSV_PATH = 'states/50_states.csv'
IMG_PATH = 'states/blank_states_img.gif'

states = p.read_csv(STATES_CSV_PATH)
state_x = states[states.state == "Alabama"].x.item()
states_list = states.state.to_list()
screen = t.Screen()
screen.title('U.S. States Game')
screen.addshape(IMG_PATH)
t.shape(IMG_PATH)

writer = t.Turtle()
writer.up()
writer.ht()

correct_answers = 0
states_list_length = len(states_list)

while correct_answers != states_list_length:
    answer_state = screen.textinput(title=f'{correct_answers}/{states_list_length} Guess the State', prompt="What's the other states correct names?").title()
    if answer_state == 'Exit':
        break
    for item in states_list:
        if answer_state == item:
            answer_x = states[states.state == answer_state].x.item()
            answer_y = states[states.state == answer_state].y.item()
            correct_answers += 1
            writer.goto(answer_x, answer_y)
            writer.write(answer_state)
            states_list.remove(item)
        

if len(states_list) == 0:
    print('You got it! Nice.')
else:
    print('We have saved the missed states for you to study later!')
    states_to_csv = {'states': states_list}
    states_df = p.DataFrame(states_to_csv)
    states_df.to_csv('./states/missed_states/states.csv')

