from time import sleep
from graphics import *
import collections
import math

dx, dy = 1, 1
win = GraphWin("moving", 640, 480)
hWin = win.getHeight()
wWin = win.getWidth()

center = win.getMouse()
c0 = Circle(center, 40)
c0.draw(win)
r0 = c0.getRadius()
rightBorder = wWin - r0
downBorder = hWin - r0
r = g = b = 0
while True:
    if (c0.getCenter().x <= r0 and dx < 0) or (c0.getCenter().x >= rightBorder and dx > 0):
        dx = -dx
    if (c0.getCenter().y <= r0 and dy < 0) or (c0.getCenter().y >= downBorder and dy > 0):
        dy = -dy
    c0.move(dx, dy)
    c0.setFill(color_rgb(r % 256, g, b))
    r += 1
    r %= 256
    sleep(0.01)
