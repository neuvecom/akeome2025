# title: Akeome2025
# author: neuve project
# desc: for New Year's Greetings
# site: https://github.com/neuvecom/akeome2025
# license: MIT
# version: 1.0

import pyxel
import random
import platform
import os
import sys

print('-----------------')
print('title: Akeome2025')
print('author: neuve project')
print('site: https://github.com/neuvecom/akeome2025')
print('license: MIT')
print('version: 1.0')
# print(platform.system()) # Darwin
# print(os.name) # posix
# print(sys.platform) # darwin
# print(platform.release()) # 24.1.0
print(platform.version()) # Darwin Kernel Version 24.1.0: Thu Oct 10 21:03:11 PDT 2024; root:xnu-11215.41.3~2/RELEASE_ARM64_T6020
# print(platform.platform()) # macOS-15.1.1-arm64-arm-64bit
# print(platform.platform(terse=True)) # macOS-15.1.1
# print(platform.platform(aliased=True)) # macOS-15.1.1-arm64-arm-64bit
print('> GAME OPEN')
print('-----------------')

pyxel.init(128,64,title='Akeome2025', display_scale=8)
pyxel.load("my_resource.pyxres")

# 初期化
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

# カスタム関数
def set_spawn():
    global tutu_x,tutu_y

    tutu_x = random.randint(9, 112)
    tutu_y = random.randint(9, 48)

    print('next BINGO is ' + str(tutu_x) + ':' + str(tutu_y))

# Pyxelの関数（更新）
def update():
    global x,y,status,tutu_x,tutu_y,tutu_status,isSound,isHelp,isScore,score

    # 座標の修正（X座標）
    if pyxel.mouse_x < 0:
        x = 1
    elif pyxel.mouse_x > 112:
        x = 112
    else:
        x = pyxel.mouse_x
    # 座標の修正（Y座標）
    if pyxel.mouse_y < 0:
        y = 1
    elif pyxel.mouse_y > 48:
        y = 48
    else:
        y = pyxel.mouse_y
    # 当たり判定（ゴール）
    if x == 5 and y == 5:
        status = True
    else:
        status = False
    # 当たり判定（餌）
    if x == tutu_x and y == tutu_y:
        tutu_status = True
        if score < 1000:
            score = score + 1
        else:
            score = 0
    else:
        tutu_status = False
    # モードの切り替え（サウンドのオンオフ）
    if pyxel.btnp(pyxel.KEY_SPACE):
        isSound = not isSound
        if isSound:
            pyxel.playm(1, loop=True)
        else:
            pyxel.stop()
    # モードの切り替え（デバック情報のオンオフ）
    if pyxel.btnp(pyxel.KEY_H):
        isHelp = not isHelp
    # モードの切り替え（スコアのオンオフ）
    if pyxel.btnp(pyxel.KEY_S):
        isScore = not isScore

    return

# Pyxelの関数（描画）
def draw():
    # 画面構築（ベース下）
    pyxel.cls(1) # 画面のクリア
    pyxel.blt(5, 5, 1, 0, 0, 16, 16) # ゴールの描画
    pyxel.text(11, 22, "^", 7)
    pyxel.text(11, 24, "|", 7)
    pyxel.text(6, 32, "LET'S      CAT", 7)
    # 画面構築（猫）
    pyxel.blt(x, y, 0, 0, 0, 16, 16)
    # 画面構築（ベース上）
    pyxel.text(6, 32, "      MOVE     HERE!", 7)
    pyxel.text(84, 55, "2025.01.01", 8)
    # 画面構築（餌）
    pyxel.text(tutu_x + 10, tutu_y + 6, ".", 5)
    # 画面構築（あけおめ）
    if status:
        pyxel.text(30, 12, "A HAPPY NEW YEAR!", 9)
    # 画面構築（餌ゲット）
    if tutu_status:
        pyxel.text(30, 12, "DELICIOUS!", 9)
        set_spawn()
    # 画面構築（スコアオン・オフ）
    if isScore:
        pyxel.text(84, 2, 'SCORE: ' + str(score), 13)
    # 画面構築（デバック情報オン・オフ）
    if isHelp:
        pyxel.text(1, 55, str(x) + ':' + str(y) +  ':' + str(tutu_x) + ':' + str(tutu_y) + ':' + str(tutu_status), 13)

    return

# Pyxelの実行
pyxel.run(update,draw)
