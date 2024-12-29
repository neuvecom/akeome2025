import pyxel
import random

pyxel.init(128,64)
pyxel.load("my_resource.pyxres")

x = 0
y = 0
status = False
tutu_status = False
score = 0

tutu_x = random.randint(9, 112)
tutu_y = random.randint(9, 48)

pyxel.playm(1, loop=True)

isSound = True
isHelp = False
isScore = False

# デバッグ用情報をコンソールに出力
print('BINGO is ' + str(tutu_x) + ':' + str(tutu_y))

def set_spawn():
    global tutu_x,tutu_y

    tutu_x = random.randint(9, 112)
    tutu_y = random.randint(9, 48)

    print('next BINGO is ' + str(tutu_x) + ':' + str(tutu_y))

def update():
    global x,y,status,tutu_x,tutu_y,tutu_status,isSound,isHelp,isScore,score

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

    # 当たり判定
    if x == 5 and y == 5:
        status = True
    else:
        status = False

    if x == tutu_x and y == tutu_y:
        tutu_status = True
        if score < 1000:
            score = score + 1
        else:
            score = 0
    else:
        tutu_status = False

    # モードの切り替え
    if pyxel.btnp(pyxel.KEY_SPACE):
        isSound = not isSound
        if isSound:
            pyxel.playm(1, loop=True)
        else:
            pyxel.stop()

    if pyxel.btnp(pyxel.KEY_H):
        isHelp = not isHelp

    if pyxel.btnp(pyxel.KEY_S):
        isScore = not isScore

    return

def draw():
    pyxel.cls(1)
    pyxel.blt(5, 5, 1, 0, 0, 16, 16) 
    pyxel.text(11, 22, "^", 7)
    pyxel.text(11, 24, "|", 7)

    pyxel.blt(x, y, 0, 0, 0, 16, 16)

    pyxel.text(6, 32, "LET'S MOVE CAT HERE!", 7)
    pyxel.text(84, 55, "2025.01.01", 8)

    pyxel.text(tutu_x + 10, tutu_y + 6, ".", 5)

    if status:
        # pyxel.play(0, 38)
        pyxel.text(30, 12, "A HAPPY NEW YEAR!", 9)

    if tutu_status:
        pyxel.text(30, 12, "DELICIOUS!", 9)
        set_spawn()

    if isScore:
        pyxel.text(84, 2, 'SCORE: ' + str(score), 13)

    if isHelp:
        pyxel.text(1, 55, str(x) + ':' + str(y) +  ':' + str(tutu_x) + ':' + str(tutu_y) + ':' + str(tutu_status), 13)

    return

pyxel.run(update,draw)
