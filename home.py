import time
import math
from graphics import *

def init_home():
    win_width = 640
    win_height = 480
    return GraphWin("Картина graphics. Автор: Тимофей Фёдорович", win_width, win_height)

def main():
    win: GraphWin = init_home()
    draw_backbround(win)
    draw_cloud(win, 100, 100)
    draw_sun(win)
    draw_house(win, win.getWidth() // 3, win.getHeight() * 2 // 3, 150, 200)
    draw_tree(win)
    time.sleep(3)

def draw_backbround(windows: GraphWin):
    sky = Rectangle(Point(0, 0), Point(windows.getWidth(), windows.getHeight() // 2))
    sky.setWidth(0)
    sky.setFill("blue")
    sky.draw(windows)
    ground = Rectangle(Point(0, windows.getHeight() // 2), Point(windows.getWidth(), windows.getHeight()))
    ground.setWidth(0)
    ground.setFill("lightgray")
    ground.draw(windows)

def draw_cloud(windows: GraphWin, x0, y0):
    cloud_circles = [(x0 - 30, y0, 40), (x0, y0 - 10, 50), (x0 + 30, y0, 40)]
    for x, y, r in cloud_circles:
        c_circle = Circle(Point(x, y), r)
        c_circle.setFill("white")
        c_circle.draw(windows)

def draw_sun(windows: GraphWin):
    sun = Circle(Point(windows.getWidth()*0.9, windows.getHeight()*0.12), math.sqrt(windows.getHeight()**2 + windows.getWidth()**2)/20)
    sun.setFill("yellow")
    sun.draw(windows)

def draw_house(windows: GraphWin, x0, y0, width, height):
    walls_height = height * 2 // 3
    roof_height = height - walls_height
    draw_walls(windows, x0, y0, width, walls_height)
    draw_window(windows, x0, y0 - walls_height // 3, width // 3, walls_height // 3)
    draw_roof(windows, x0, y0 - walls_height, width, roof_height)

def draw_walls(windows: GraphWin, x0, y0, width, height):
    walls = Rectangle(Point(x0 - width // 2, y0 - height), Point(x0 + width // 2, y0))
    walls.setWidth(3)
    walls.setFill("gray")
    walls.draw(windows)


def draw_window(windows: GraphWin, x0, y0, width, height):
    window = Rectangle(Point(x0 - width // 2, y0 - height), Point(x0 + width // 2, y0))
    window.setWidth(3)
    window.setFill("yellow")
    window.draw(windows)

def draw_roof(windows: GraphWin, x0, y0, width, height):
    coordinates = [(x0 - width // 2, y0), (x0, y0 - height), (x0 + width // 2, y0)]
    points = [Point(x, y) for x, y in coordinates]
    roof = Polygon(points)
    roof.setWidth(3)
    roof.setFill("darkred")
    roof.draw(windows)

def draw_tree(windows: GraphWin):
    x = windows.getWidth()
    y = windows.getHeight()
    wTree = 0.23*x # Ширина дерева
    lcTree = 0.65*x # Координата X левого угла кроны
    hTree = 0.53*y # Уровень верхней кроны
    tri = [Point(lcTree, hTree), Point(lcTree + wTree, hTree), Point(lcTree + wTree/2, hTree - math.tan(math.pi/5)*wTree/2)]
    aPol = Polygon(tri)
    aPol.setFill("green")
    aPol.setWidth(2)
    aPol.draw(windows)
    for cntPol in range(1,3):
        tmpPol = aPol.clone()
        tmpPol.move(0, cntPol*math.tan(math.pi/5)*wTree/2)
        tmpPol.draw(windows)
    print(*tri[0])

main()