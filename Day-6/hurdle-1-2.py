# turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()


# hurdle 1 and hurdle 2
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    jump()
