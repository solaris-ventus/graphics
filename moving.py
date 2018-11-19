from time import sleep
from graphics import *
import collections
import math

dx, dy = -1, -1
win = GraphWin("moving", 800, 600)
wWin = win.getWidth()
hWin = win.getHeight()

# Точка ценра
center = win.getMouse()
win.plotPixel(*center, "white")

# Произольная точка окружности
twoPoint = win.getMouse()
win.plotPixel(*twoPoint, "white")

# Считаем радиус по центру по двум точкам. Берем целую часть
r0 = math.sqrt((twoPoint.x - center.x)**2 + (twoPoint.y - center.y)**2) // 1
print(r0)

# Считаем правую и нижнюю границу в зависемости от размеров холста. Левую и верхнюю отсчитываем от нуля тк по умолчанию
# начало координат в левом-верхнем углу холста
rightBorder = wWin - r0
downBorder = hWin - r0

c0 = Circle(center, r0).draw(win)
while True:
    # Проверяем что при движении влево (dx, dy < 0) не выйдем за границы при следующем смещении и
    # при движении вправо так же не выйдем за границы при следующем спещении
    if (c0.getCenter().x <= r0 and dx < 0) or (c0.getCenter().x >= rightBorder and dx > 0):
        dx = -dx
    if (c0.getCenter().y <= r0 and dy < 0) or (c0.getCenter().y >= downBorder and dy > 0):
        dy = -dy
    # Смещение на dx, dy
    c0.move(dx, dy)
    c0.setFill(color_rgb(int(c0.getCenter().x) // 2 % 256, int(c0.getCenter().y) // 2 % 256, 100))
    sleep(0.002)
    # Отладочный проверка выхода за гранизу
    if c0.getCenter().x < r0 - 1 or c0.getCenter().x > wWin + 1 - r0 \
            or c0.getCenter().y < r0 - 1 or c0.getCenter().y > hWin + 1 - r0:
        print("Текущие координаты центра окружности:", c0.getCenter(), "\nРадиус окружности:", c0.getRadius(), "\nРазер холста:", win.getWidth(), win.getHeight())
        break
