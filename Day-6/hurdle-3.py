# turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()


# hurdle 3
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
