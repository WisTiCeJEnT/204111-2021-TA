LAB = "turtlelab9.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}",LAB)

from turtlelab9 import turtle,check

for i in range(8):
    turtle.left(45)
    for j in range(5):
        turtle.forward(50)
    turtle.backward(50*5)

check()