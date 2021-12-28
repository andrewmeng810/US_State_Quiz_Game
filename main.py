import turtle as t
import pandas as pd
import StateManager as s

"""
1. concert the guess to title case
2. check if the guess is among the 50 states
3. write correct guesses onto the map
4. use a loop to allow the user to keep guessing
5. record the correct guesses in a list
6. keep track of the score
"""

# Create canvas
screen = t.Screen()
screen.title('U.S. States Games')
image = 'blank_states_img.gif'
screen.addshape(image)
t.shape(image)
screen.tracer(0)

# create state manager
state = s.StateManager()


state_data = pd.read_csv('50_states.csv')
all_states = state_data.state.tolist()


is_game_on = True

while is_game_on:
    answer_state = screen.textinput(title='{}/50 States Correct'.format(len(state.state_list)),
                                    prompt="What is another state's name").title()
    if answer_state.lower() == 'exit':
        break

    if answer_state in all_states:
        state.show_state(answer_state,
                         state_data[state_data.state == answer_state]['x'].item(),
                         state_data[state_data.state == answer_state]['y'].item())

    screen.update()


# screen.exitonclick()
