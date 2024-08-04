import turtle
import pandas

screen = turtle.Screen()
screen.title("India States Game")
image = "mainn\python\d25_csv\INDIA_STATES\india_map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("mainn\python\d25_csv\INDIA_STATES\states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 28:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/28 states guessed.", prompt="What's another state's name?\nType 'exit' to end the game.").title()
    print(answer_state)

    if answer_state == "Exit":
        # # To create a csv file of the states which were not guessed
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        # new_data = pandas.DataFrame(missing_states)
        # new_data.to_csv("missed_states.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
