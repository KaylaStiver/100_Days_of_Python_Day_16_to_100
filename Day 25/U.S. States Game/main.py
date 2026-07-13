import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
us_map = turtle.shape(image)

data = pandas.read_csv("./50_states.csv")
data.state = data.state.str.lower()
data.x = data.x.astype(float)
data.y = data.y.astype(float)
correct_answer_list = []
user_answer = ""

while len(correct_answer_list) < len(data):
    user_answer = turtle.textinput(f"{len(correct_answer_list)}/50 correct", "Enter a state")
    if user_answer is not None:
        user_answer = user_answer.lower()
    for row in data.itertuples():
        if user_answer == row.state and user_answer not in correct_answer_list:
            correct_answer_list.append(row.state)
            state_xcor = float(row.x)
            state_ycor = float(row.y)
            state_text = turtle.Turtle()
            state_text.penup()
            state_text.hideturtle()
            state_text.goto(state_xcor, state_ycor)
            state_text.write(f"{row.state}", align="center", font=("Courier", 12, "normal"))

turtle.mainloop()

