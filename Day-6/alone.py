# turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()


# draw square
def draw_square():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_right()
    move()


draw_square()
