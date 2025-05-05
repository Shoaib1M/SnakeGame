import turtle
move_distance=20
UP=90
LEFT=180
DOWN=270
RIGHT=0
starting_position=[(0,0),(-20,0),(-40,0)]
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        position=0
        for i in starting_position:
            self.add_segment(i)
        self.segments[0].color('red')

    def move(self,move_distance):
            for i in range(len(self.segments) - 1, 0, -1):
                x = self.segments[i - 1].xcor()
                y = self.segments[i - 1].ycor()
                self.segments[i].goto(x, y)
            self.segments[0].forward(move_distance)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position):
        t = turtle.Turtle()
        t.shape("square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.segments.append(t)




