import pyxel

pyxel.init(128,64)
pyxel.load("my_resource.pyxres")

x = 0
y = 0
status = 0
pyxel.playm(1, loop=True)

def update():
    global x,y,status

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
        
    return

def draw():
    pyxel.cls(1)
    pyxel.blt(5, 5, 1, 0, 0, 16, 16) 
    pyxel.text(11, 22, "^", 7)
    pyxel.text(11, 24, "|", 7)
    pyxel.text(6, 32, "LET'S MOVE CAT HERE!", 7)
    pyxel.text(84, 55, "2025.01.01", 8)

    pyxel.blt(x, y, 0, 0, 0, 16, 16)

    if status == 1:
        # pyxel.play(0, 38)
        pyxel.text(30, 12, "A HAPPY NEW YEAR!", 9)

    return

pyxel.run(update,draw)
