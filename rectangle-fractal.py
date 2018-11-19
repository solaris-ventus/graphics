# import graphics
from time import sleep
from graphics import *

α = 0.04

depth = 10

def main(A,B,C,D,depth=10):
    if depth < 1:
        return
    for M, N in (A, B), (B, C), (C, D), (D, A):
        aline = Line(Point(*M), Point(*N))
        aline.setFill("green")
        aline.draw(win)
    else:
        A1 = (A[0]+α*(B[0]-A[0]), A[1]+α*(B[1]-A[1]))
        C1 = (C[0]+α*(D[0]-C[0]), C[1]+α*(D[1]-C[1]))
        B1 = (B[0]+α*(C[0]-B[0]), B[1]+α*(C[1]-B[1]))
        D1 = (D[0]+α*(A[0]-D[0]), D[1]+α*(A[1]-D[1]))
        main(A1, B1, C1, D1, depth-1)

win = GraphWin("test", 400, 400)
win.setBackground("white")

main((100, 300), (100, 100), (300, 100), (300, 300), 450)
win.getMouse()