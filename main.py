import turtle
import pandas

screen = turtle.Screen()
screen.title("India States Game")
image = "mainn\python\d25_csv\INDIA_STATES\indiaa.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("mainn\python\d25_csv\INDIA_STATES\states.csv")


answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?")
print(answer_state)






screen.exitonclick()