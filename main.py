import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

###
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)#
# turtle.mainloop()
###

while len(guessed_states) < 50:
    if len(guessed_states) == 0:
        answer_state = screen.textinput("Guess the States", "What's another state's name?").title()
    else:
        answer_state = screen.textinput(f"{len(guessed_states)}/50 States Correct",
                                        "What's another state's name?").title()
    print("You typed: " + answer_state)

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        print(missing_states)
        pandas.DataFrame(missing_states).to_csv("missing_states.cvs")
        break
    elif answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(float(state_data.x), float(state_data.y))
        t.write(answer_state, False, "center", ("Arial", 10, "normal"))

# pandas"states_to_learn.csv"

