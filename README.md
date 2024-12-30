# akeome2025
for New Year's Greetings.

- [デモ](https://neuvecom.github.io/akeome2025/)
- [解説記事](https://zenn.dev/neuvecom/articles/0ab7a54b5f2d97)

## はじめに
このリポジトリは、上記リンクのあけおめ記事のソースコードです。  
Macでの実行を想定しています（Windowsでの検証はできてません）。  
アプリの書き出しやスマホ端末の対応は未検証でテスト中ですので参考程度に。

> 記事のソースはzennディレクトリにあります

## 操作方法
機能が増えてきたので操作方法を記載
- 猫の移動
  - 矢印キーもしくはASDWで移動可能
- サウンドのオン・オフ
  - スペースバーもしくはBボタンでオン・オフできます
    - 曲の最初から再生しなおします
- スコア表示のオン・オフ
  - XキーもしくはXボタンでオン・オフできます
- 自動プレイのオン・オフ
  - PキーもしくはAボタンでオン・オフできます
- デバック情報のオン・オフ
  - HキーもしくはYボタンでオン・オフできます

## メモ
- エディタを開く `uv run pyxel edit`  
- 起動する `uv run pyxel run ./Akeome2025/akeome.py`
  - 自動更新で起動 `uv run pyxel watch ./Akeome2025 ./Akeome2025/akeome**.py`
- pyxapp化 `uv run pyxel package . akeome.py` <= `cd Akeome2025`
  - 実行前に不要なファイルは削除（古いHTMLやpyxappなど）
- html出力 `uv run pyxel app2html Akeome2025.pyxapp` <= `cd Akeome2025`
  - 出力後にファイル名をindex.htmlに変更
- pyxapp化後、アプリを起動 `uv run pyxel play Akeome2025.pyxapp` <= `cd Akeome2025`
- ビルドスクリプト起動 `zsh build.sh`

## 環境構築
- `uv sync` Githubからダウンロードした場合
- `uv init` 既存のフォルダでUvを導入する場合
  - `uv add pyxel` 忘れずに実行
