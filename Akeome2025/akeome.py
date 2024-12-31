# title: Akeome2025
# author: neuve project
# desc: for New Year's Greetings
# site: https://github.com/neuvecom/akeome2025
# license: MIT
# version: 1.0

import pyxel
import random

# ===============
# ---- 初期化 ----
# ===============

# プロジェクト全般
myname = 'Akeome2025'
my_resource = 'my_resource.pyxres'
x_max = 128
y_max = 64

# プレイ関連の初期値
safe_ajst = 14 # 餌の出現ポイントの調整
x = 5 # 猫の初期出現X軸の値
y = 40 # 猫の初期出現Y軸の値
status = False
tutu_status = False
score = 0
# 餌の出現ポイントをランダムに設定
tutu_x = random.randint(safe_ajst, x_max - safe_ajst - 2)
tutu_y = random.randint(safe_ajst, y_max - safe_ajst - 2)

# ---- ゲーム初期化 ----
pyxel.init(x_max,y_max,title=myname, display_scale=4) # ウィンドウの初期化
pyxel.load(my_resource) # リソースの読込
pyxel.playm(1, loop=True) # BGMの再生

# 状態の初期化
isSound = True # 音声再生
isHelp = False # ヘルプ表示
isScore = False # スコア表示
isAuto = False  # 自動プレイ
isClear = False # ゲームクリア（スコアが500以上になったか）

# 各機能用の初期値設定
deli_timer = 0 # DELICIOUSの文字を表示するタイマー
happy_timer = 0 # HAOOY NEW YEAR!の文字を表示するタイマー
time_val = 3 * 60 # タイマーの設定値（3秒）:60fpsの想定
clear_cnt = 0 # 餌を取った数（背景の色指定に使用）
bgcolor_list = [1,3,5,11,13] # 背景の色のリスト
random.shuffle(bgcolor_list) # 背景の色のリストをシャッフル
clear_cat_ajst = 0 # エンドカードの猫の位置の調整値の初期値

# デバッグ用情報をコンソールに出力
print('BINGO is ' + str(tutu_x).zfill(3) + ':' + str(tutu_y).zfill(3))

# 背景追加アイテムの出現ポイントの決定
item_point = [[10,41],[37,41],[61,41],[98,24]] # 出現ポイントのリスト
random.shuffle(item_point) # 出現ポイントのリストをシャッフル
print(item_point) # 出現ポイントのリストをコンソールに出力

# ====================
# ---- カスタム関数 ----
# ====================

# 餌を置く
def set_spawn():
    global tutu_x,tutu_y
    # 餌の出現ポイントをランダムに設定
    tutu_x = random.randint(safe_ajst, x_max - safe_ajst - 2)
    tutu_y = random.randint(safe_ajst, y_max - safe_ajst - 2)
    # 結果をコンソールに出力
    print('next BINGO is ' + str(tutu_x).zfill(3) + ':' + str(tutu_y).zfill(3) + ' / Score: ' + str(score).zfill(3))

# 自動プレイ
def auto_drive():
    global x,y,tutu_x,tutu_y
    # 除算の余りで0/1を取得
    axus = random.randint(0, 500) % 2
    # x軸か、y軸のみを変更することでジリジリ猫を動かす
    if axus:
        if x > tutu_x:
            x = x - 1
        elif x == tutu_x:
            x = tutu_x
        else:
            x = x + 1
    else:
        if y > tutu_y:
            y = y - 1
        elif y == tutu_y:
            y = tutu_y
        else:
            y = y + 1

# エンドカード
def game_clear():
    pyxel.cls(1) # 画面のクリア
    pyxel.text(10, 5, "THANK YOU FOR YOUR PLAYING.", 7)
    pyxel.text(6, 16, "BEST WISHES FOR THE NEW YEAR!!", 0)
    pyxel.text(5, 15, "BEST WISHES FOR THE NEW YEAR!!", 9)
    pyxel.blt(58 + clear_cat_ajst, 23, 0, 0, 0, 16, 16, 1)
    pyxel.blt(24, 44, 2, 0, 0, 16, 16, 1)
    pyxel.blt(44, 44, 2, 16, 0, 16, 16, 1)
    pyxel.blt(64, 44, 2, 32, 0, 16, 16, 1)
    pyxel.blt(84, 44, 2, 48, 0, 16, 16, 1)

# ゲームメイン処理
def play_game():
    # 画面構築
    pyxel.cls(bgcolor_list[clear_cnt]) # 画面のクリア
    # 背景にアイテム追加(もっときれいに書きたい)
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
        pyxel.text(84, 2, 'SCORE: ' + str(score).zfill(3), 7)
    # 画面構築（自動プレイ）
    if isAuto:
        pyxel.text(81, 55, '.', 10)
    # 画面構築（餌）
    pyxel.text(tutu_x + 10, tutu_y + 6, ".", 4)

    return

# ===========================
# ---- Pyxelの関数（更新） ----
# ===========================

def update():
    global x,y,status,tutu_x,tutu_y,tutu_status
    global isSound,isHelp,isScore,isAuto,isClear
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
        happy_timer = 0
        deli_timer = int(time_val / 3)
        score = score + 10
        if score < 500:
            if clear_cnt > 3:
                clear_cnt = 0
            else:
                clear_cnt = clear_cnt + 1
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
    if score > 499:
        isClear = True
        # クリア画面の猫のX座標更新
        if clear_cat_ajst > 65:
            clear_cat_ajst = -65
        else:
            clear_cat_ajst = clear_cat_ajst + 1
        # クリア画面
        game_clear()

# ===========================
# ---- Pyxelの関数（描画） ---- 
# ===========================

def draw():

    if isClear:
        game_clear()
    else:
        play_game()

    # 画面構築（デバック情報オン・オフ）
    if isHelp:
        pyxel.text(1, 46, str(deli_timer).zfill(3) + ':' + str(happy_timer).zfill(3) + ':' + str(isClear), 7)
        pyxel.text(1, 55, str(x).zfill(3) + ':' + str(y).zfill(3) +  '=>' + str(tutu_x).zfill(3) + ':' + str(tutu_y).zfill(3), 7)

    return

# ====================
# ---- Pyxelの実行 ----
# ====================

pyxel.run(update,draw)
