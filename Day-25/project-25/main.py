# Project 25
# US States Quiz

# ------------------------------------------------------------------------------------------------------------------------------------------
import turtle
import pandas

""" 
# on mouse click print the coordinates of mouse  
def get_mouse_click_coor(x,y):
    print(x,y)

turtle.onscreenclick(get_mouse_click_coor)
"""

# Making Screen
screen = turtle.Screen()
screen.title("U.S States Game")

# adding image to turtle screen
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# reading csv file and converting it's data into a list
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

# list of guessed states
guessed_states = []

# game is on till the user guess all the states
while len(guessed_states) < 50:
    # asking for the state name
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    # secret input to exit the game
    if answer_state == "Exit":
        missing_states = []

        # if user guessed wrong state
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)

        # making a csv file of missing states to learn
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # if user guessed the correct state
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        # t.goto(int(state_data.x), int(state_data.y)) # Deprecated Code
        t.goto(int(state_data.x.iloc[0]), int(
            state_data.y.iloc[0]))  # Latest Code
        t.write(answer_state)


screen.exitonclick()
# ------------------------------------------------------------------------------------------------------------------------------------------
