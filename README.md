# akeome2025
for New Year's Greetings.

- [デモ](https://neuvecom.github.io/akeome2025/)
- [解説記事](https://zenn.dev/neuvecom/articles/0ab7a54b5f2d97)

## メモ
- エディタを開く `uv run pyxel edit`  
- 起動する `uv run pyxel run akeome.py`
- pyxapp化 `uv run pyxel package . akeome.py`
  - 実行前に不要なファイルは削除（古いHTMLやpyxappなど）
- html出力 `uv run pyxel app2html akeome2025.pyxapp`
  - 出力後にファイル名をindex.htmlに変更
- ビルドスクリプト起動 `zsh build.sh`