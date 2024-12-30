# ライブラリの読込
import pyxel

# ステージサイズの設定
pyxel.init(128, 64)
# リソースの読込
pyxel.load("my_resource.pyxres")

# 使用する変数の初期化
x = 0
y = 0
status = 0

# 更新処理（1秒に60回実行）
def update():
    # 値を更新するので、グローバルとして変数を読込？
    # 指定？宣言？スコープを明示？
    # 言い方はわかりませんが、必要
    global x,y,status
    # マウスの座標で更新
    x = pyxel.mouse_x 
    y = pyxel.mouse_y
    #マウスの位置でステータスの変更
    if x == 5 and y == 5: 
        status = 1
    else:
        status = 0
    # 処理終了
    return

# 描画処理
def draw():
    # 画面を1番の色で塗りつぶす
    pyxel.cls(1)
    # 1番のスプライト（枠の画像）を配置
    pyxel.blt(5, 5, 1, 0, 0, 16, 16) 
    # 文字を配置
    pyxel.text(11, 22, "^", 7)
    pyxel.text(11, 24, "|", 7)
    pyxel.text(6, 32, "LET'S MOVE CAT HERE!", 7)
    pyxel.text(84, 55, "2025.01.01", 8)
    # 0番のスプライト（猫の画像）を配置
    pyxel.blt(x, y, 0, 0, 0, 16, 16)
    # 条件によっては文字を配置
    if status == 1:
        pyxel.text(30, 12, "A HAPPY NEW YEAR!", 9)
    # 処理終了
    return

# Pyxelの起動
pyxel.run(update,draw) 