LAB = "turtlelab8.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}",LAB)

from turtlelab8 import turtle,radar,check

r = radar.ball_direction()
D = {'e': 0, 'ne': 45, 'n': 90, 'nw': 135, 'w': 180, 'sw': 225, 's': 270, 'se': 315}
while(r != 'x'):
    turtle.left(D[r])
    turtle.forward(1)
    turtle.right(D[r])
    r = radar.ball_direction()

check()

