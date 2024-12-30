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
# print(platform.version()) # Darwin Kernel Version 24.1.0: Thu Oct 10 21:03:11 PDT 2024; root:xnu-11215.41.3~2/RELEASE_ARM64_T6020
# print(platform.platform()) # macOS-15.1.1-arm64-arm-64bit
# print(platform.platform(terse=True)) # macOS-15.1.1
# print(platform.platform(aliased=True)) # macOS-15.1.1-arm64-arm-64bit
print('> GAME OPEN')
print('-----------------')

# 初期化
myname = 'Akeome2025'
my_resource = 'my_resource.pyxres'
x_max = 128
y_max = 64
safe_ajst = 14
x = 5
y = 40
status = False
tutu_status = False
score = 0

tutu_x = random.randint(safe_ajst, x_max - safe_ajst - 2)
tutu_y = random.randint(safe_ajst, y_max - safe_ajst - 2)

# ゲーム初期化
pyxel.init(x_max,y_max,title=myname, display_scale=4)
pyxel.load(my_resource)
pyxel.playm(1, loop=True)

isSound = True
isHelp = False
isScore = False
isAuto = False
isClear = False

deli_timer = 0
happy_timer = 0
time_val = 3 * 60
clear_cnt = 0
bgcolor_list = [1,3,5,11,13]
random.shuffle(bgcolor_list)
clear_cat_ajst = 0

# デバッグ用情報をコンソールに出力
print('BINGO is ' + str(tutu_x).zfill(3) + ':' + str(tutu_y).zfill(3))

# 背景追加アイテムの出現ポイントの決定
item_point = [[10,41],[37,41],[61,41],[98,24]]
random.shuffle(item_point)
print(item_point)

# カスタム関数
def set_spawn():
    global tutu_x,tutu_y

    tutu_x = random.randint(safe_ajst, x_max - safe_ajst - 2)
    tutu_y = random.randint(safe_ajst, y_max - safe_ajst - 2)

    print('next BINGO is ' + str(tutu_x).zfill(3) + ':' + str(tutu_y).zfill(3) + ' / Score: ' + str(score).zfill(3))

def auto_drive():
    global x,y,tutu_x,tutu_y

    axus = random.randint(0, 500) % 2
    if axus:
        if x > tutu_x:
            x = x - 1
        else:
            x = x + 1
    else:
        if y > tutu_y:
            y = y - 1
        else:
            y = y + 1

# Pyxelの関数（更新）
def update():
    global x,y,status,tutu_x,tutu_y,tutu_status
    global isSound,isHelp,isScore,isAuto
    global score,deli_timer,happy_timer,clear_cnt
    global clear_cat_ajst

    # 当たり判定（ゴール）
    if x == 5 and y == 5:
        status = True
        happy_timer = time_val
        deli_timer = 0
    else:
        status = False
    # 当たり判定（餌）
    if x == tutu_x and y == tutu_y:
        tutu_status = True
        if score < 500:
            score = score + 1
            happy_timer = 0
            deli_timer = int(time_val / 3)
            if clear_cnt > 3:
                clear_cnt = 0
            else:
                clear_cnt = clear_cnt + 1
        else:
            isClear = True
    else:
        tutu_status = False
    # モードの切り替え（サウンドのオンオフ）
    if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_B):
        isSound = not isSound
        if isSound:
            pyxel.playm(1, loop=True)
        else:
            pyxel.stop()
    # モードの切り替え（デバック情報のオンオフ）
    if pyxel.btnp(pyxel.KEY_Y) or pyxel.btnp(pyxel.KEY_H) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_Y):
        isHelp = not isHelp
    # モードの切り替え（スコアのオンオフ）
    if pyxel.btnp(pyxel.KEY_X) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_X):
        isScore = not isScore
    # モードの切り替え（自動プレイ）
    if pyxel.btnp(pyxel.KEY_P) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_A):
        isAuto = not isAuto
    # 操作系の切り替え
    if isAuto:
        # 自動プレイ
        auto_drive()
    else:
        # ゲームパッド対応＆キー操作対応
        if pyxel.btn(pyxel.KEY_W) or pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP):
            y = y - 1
        if pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):
            y = y + 1
        if pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
            x = x - 1
        if pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
            x = x + 1
    # 座標の修正（X座標）
    if x < 0:
        x = 0
    elif x > 112:
        x = 112
    else:
        x = x
    # 座標の修正（Y座標）
    if y < 0:
        y = 0
    elif y > 48:
        y = 48
    else:
        y = y
    # 文字表示のタイマー更新（餌）
    if deli_timer:
        deli_timer = deli_timer - 1
    # 文字表示のタイマー更新（あけおめ）
    if happy_timer:
        happy_timer = happy_timer - 1
    # クリア画面の猫のX座標更新
    if clear_cat_ajst > 65:
        clear_cat_ajst = -65
    else:
        clear_cat_ajst = clear_cat_ajst + 1

    return

# Pyxelの関数（描画）
def draw():

    if isClear:
        pyxel.cls(1) # 画面のクリア
        pyxel.text(10, 5, "THANK YOU FOR YOUR PLAYING.", 7)
        pyxel.text(6, 16, "BEST WISHES FOR THE NEW YEAR!!", 0)
        pyxel.text(5, 15, "BEST WISHES FOR THE NEW YEAR!!", 9)
        pyxel.blt(58 + clear_cat_ajst, 23, 0, 0, 0, 16, 16, 1)
        pyxel.blt(24, 44, 2, 0, 0, 16, 16, 1)
        pyxel.blt(44, 44, 2, 16, 0, 16, 16, 1)
        pyxel.blt(64, 44, 2, 32, 0, 16, 16, 1)
        pyxel.blt(84, 44, 2, 48, 0, 16, 16, 1)
    else:
        # 画面構築
        pyxel.cls(bgcolor_list[clear_cnt]) # 画面のクリア
        # 背景にアイテム追加
        if score > 100:
            pyxel.blt(item_point[0][0], item_point[0][1], 2, 0, 0, 16, 16, 1)
        if score > 200:
            pyxel.blt(item_point[1][0], item_point[1][1], 2, 16, 0, 16, 16, 1)
        if score > 300:
            pyxel.blt(item_point[2][0], item_point[2][1], 2, 32, 0, 16, 16, 1)
        if score > 400:
            pyxel.blt(item_point[3][0], item_point[3][1], 2, 48, 0, 16, 16, 1)
        # ゴールの描画
        pyxel.blt(5, 5, 1, 0, 0, 16, 16, 0) 
        # 背景文字の描画（猫より後）
        pyxel.text(11, 22, "^", 7)
        pyxel.text(11, 24, "|", 7)
        pyxel.text(6, 32, "LET'S      CAT", 7)
        # 画面構築（猫）
        pyxel.blt(x, y, 0, 0, 0, 16, 16, 1)
        # 背景文字の描画（猫より前）
        pyxel.text(6, 32, "      MOVE     HERE!", 7)
        pyxel.text(84, 55, "2025.01.01", 8)
        # 画面構築（あけおめ）
        if status or happy_timer:
            pyxel.text(31, 13, "A HAPPY NEW YEAR!", 0)
            pyxel.text(30, 12, "A HAPPY NEW YEAR!", 9)
        # 画面構築（餌ゲット）
        if (tutu_status or deli_timer) and (not status or not happy_timer):
            pyxel.text(31, 13, "DELICIOUS!", 0)
            pyxel.text(30, 12, "DELICIOUS!", 9)
        # 餌リセット
        if tutu_status:
            set_spawn()
        # 画面構築（スコアオン・オフ）
        if isScore:
            pyxel.text(84, 2, 'SCORE: ' + str(score).zfill(3), 13)
        # 画面構築（デバック情報オン・オフ）
        if isHelp:
            pyxel.text(1, 46, str(deli_timer) + ':' + str(happy_timer), 13)
            pyxel.text(1, 55, str(x) + ':' + str(y) +  ':' + str(tutu_x) + ':' + str(tutu_y), 13)
        # 画面構築（自動プレイ）
        if isAuto:
            pyxel.text(81, 55, '.', 10)
        # 画面構築（餌）
        pyxel.text(tutu_x + 10, tutu_y + 6, ".", 4)

    return

# Pyxelの実行
pyxel.run(update,draw)
