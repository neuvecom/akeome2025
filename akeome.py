import pyxel
import random

pyxel.init(128,64)
pyxel.load("my_resource.pyxres")

x = 0
y = 0
status = 0
tutu_status = 0

pyxel.playm(1, loop=True)

tutu_x = random.randint(1, 112)
tutu_y = random.randint(1, 48)

print('BINGO is ' + str(tutu_x) + ':' + str(tutu_y))

def update():
    global x,y,status,tutu_x,tutu_y,tutu_status

    # 座標の修正
    if pyxel.mouse_x < 0:
        x = 1
    elif pyxel.mouse_x > 112:
        x = 112
    else:
        x = pyxel.mouse_x

    if pyxel.mouse_y < 0:
        y = 1
    elif pyxel.mouse_y > 48:
        y = 48
    else:
        y = pyxel.mouse_y

    if x == 5 and y == 5:
        status = 1
    else:
        status = 0

    if x == tutu_x and y == tutu_y:
        tutu_status = 1
    else:
        tutu_status = 0

    return

def draw():
    pyxel.cls(1)
    pyxel.blt(5, 5, 1, 0, 0, 16, 16) 
    pyxel.text(11, 22, "^", 7)
    pyxel.text(11, 24, "|", 7)
    pyxel.text(6, 32, "LET'S MOVE CAT HERE!", 7)
    pyxel.text(84, 55, "2025.01.01", 8)
    pyxel.text(1, 55, str(x) + ':' + str(y) +  ':' + str(tutu_x) + ':' + str(tutu_y) + ':' + str(tutu_status), 7)

    pyxel.blt(x, y, 0, 0, 0, 16, 16)

    if status == 1:
        # pyxel.play(0, 38)
        pyxel.text(30, 12, "A HAPPY NEW YEAR!", 9)

    if tutu_status == 1:
        pyxel.text(30, 12, "BINGO!", 9)

    return

pyxel.run(update,draw)
