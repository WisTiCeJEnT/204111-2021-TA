LAB = "turtlelab7.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}.2",LAB)

from turtlelab7 import turtle,check

def make_polygon(n,size):
    """commands the Turtle to make a regular polygon of n sides with the size specified"""
    """ 
    n = number of vertices
    Internal angles = 180 * (n - 2)
    Angle each = Internal angles / n = (180 * (n - 2)) / n
    Each turn = 180 - each internal angle = 180 - ((180 * (n - 2)) / n) = 360 / n
    """
    for i in range(n):
        turtle.forward(size)
        turtle.left(360 / n)

check()