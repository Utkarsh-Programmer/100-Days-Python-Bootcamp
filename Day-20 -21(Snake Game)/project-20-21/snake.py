from turtle import Turtle

# starting positions of snake segments
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

# snake move distance
MOVE_DISTANCE = 20

# snake directions
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """This class is responsible for making snake and moving snake."""

    def __init__(self):
        # snake segments
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """This function makes snake."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """This function add a segments to the snake body each time it collides with food."""
        new_segment = Turtle("square")
        new_segment.color("coral")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """This function extends the snake height by adding a segment to the end position."""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """This function moves snake."""
        for segment_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[segment_num-1].xcor()
            new_y = self.segments[segment_num-1].ycor()
            self.segments[segment_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """This function moves snake up."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """This function moves snake down."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """This function moves snake left."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """This function moves snake right."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
