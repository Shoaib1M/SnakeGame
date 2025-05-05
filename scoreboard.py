from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.point=Turtle()
        self.color("white")
        self.penup()
        self.goto(0,250)
        self.hideturtle()
        self.write(f"Points: {self.score}",align="center",font=("Arial",25,"normal"))



    def detected(self):
        self.clear()
        self.score+=1
        self.goto(0, 250)
        self.hideturtle()
        self.write(f"Points: {self.score}",align="center",font=("Arial",25,"normal"))

    def game_over(self):
        game_over_text = Turtle()
        game_over_text.color("white")
        game_over_text.goto(0, 0)
        game_over_text.penup()
        game_over_text.hideturtle()
        game_over_text.write("Game Over.", align="center", font=("Arial", 24, "bold"))