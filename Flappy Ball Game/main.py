import pgzrun
import random

TITLE = "Flappy Ball Game"
WIDTH = 800
HEIGHT = 600
GRAVITY = 2000.00




class Ball():
    def __init__(self, initial_x, initial_y, radius):
        self.initial_x = initial_x
        self.initial_y = initial_y
        self.radius = radius
        self.velocity_x = 200
        self.velocity_y = 0
    def display(self):
        pos = (self.initial_x,self.initial_y)
        screen.draw.filled_circle(pos,self.radius,"blue")

ball = Ball(300,400,50)

def draw():
   screen.clear()
   ball.display() 

def update(dt):
    uy = ball.velocity_y
    ball.velocity_y += GRAVITY*dt
    ball.initial_y += (uy+ball.initial_y)*0.5*dt

    if ball.initial_y > HEIGHT-ball.radius:
        ball.initial_y = HEIGHT-ball.radius
        ball.velocity_y = -ball.velocity_y*0.9
        
    ball.initial_x += ball.velocity_x*dt
    if ball.initial_x > WIDTH-ball.radius or ball.initial_x < ball.radius:
        ball.velocity_x = -ball.velocity_x

def on_key_down(key):
    if key == keys.SPACE:
        ball.velocity_y = -500 


pgzrun.go()