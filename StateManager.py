import turtle as t

ALIGNMENT = 'center'
FONT = ('Courier', 10, 'normal')


class StateManager:
    def __init__(self):
        self.state_list = []

    def show_state(self, state_name, state_x, state_y):
        new_state = t.Turtle()
        new_state.penup()
        new_state.goto(state_x, state_y)
        new_state.write('{}'.format(state_name), move=False, align=ALIGNMENT, font=FONT)
        new_state.hideturtle()
        self.state_list.append(new_state)
