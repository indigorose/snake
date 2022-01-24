from turtle import Turtle

START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    # Creating the starting snake of three blocks.
    def __init__(self):
        self.snake_piece = []
        self.create_snake()
        self.head = self.snake_piece[0]

    def create_snake(self):
        for position in START_POS:
            self.add_tail(position)

    def add_tail(self, position):
        snake_body = Turtle(shape="square")
        snake_body.color("white")
        snake_body.penup()
        snake_body.goto(position)
        self.snake_piece.append(snake_body)

    def extend(self):
        self.add_tail(self.snake_piece[-1].position())

    def move(self):
        for piece_num in range(len(self.snake_piece) - 1, 0, -1):
            new_x = self.snake_piece[piece_num - 1].xcor()
            new_y = self.snake_piece[piece_num - 1].ycor()
            self.snake_piece[piece_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
