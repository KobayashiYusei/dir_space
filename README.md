# dir_space
[![test](https://github.com/KobayashiYusei/dir_space/actions/workflows/test.yml/badge.svg)](https://github.com/KobayashiYusei/dir_space/actions/workflows/test.yml)
[![GitHub License](https://img.shields.io/github/license/KobayashiYusei/numberGuesser)](LICENSE)
<img src="https://img.shields.io/badge/ -Python-F9DC3E.svg?logo=python">

## 概要
- ガウス＝ザイデル法によって連立方程式の解を求めるコマンドです。
- 係数行列と右辺を入力することで多元連立方程式の解を求めることが出来ます。
- ガウス＝ザイデル法は以下の式で表され、適当な初期値を代入することで得られた解を再帰的に変数に代入して連立方程式の解を求めていく手法です。

## 対応環境
- **OS**
    - Ubuntu 22.04.1 LTS
- **Python**
    - 3.7 ~ 3.10

## インストール
コマンドラインで以下を実行します。
```bash
$ git clone https://github.com/KobayashiYusei/gaussSeidel.git
$ cd gaussSeidel
$ chmod 755 gusdl
```

## 使い方
```bash
$ echo '[{方程式1の係数行列}]　[{方程式2の係数行列}]　[{方程式3の係数行列}]...  [{右辺の解行列}]' | ./gusdl
```
- 連立方程式の係数行列を順番に入力していきます。
- 最後に解の行列を入力して実行します。
- ガウス＝ザイデル法によって収束しない方程式は解くことは出来ません。

### 実行例
```bash
$ echo '[4, -1, 0, 0] [-1, 4, -1, 0] [0, -1, 4, -1] [0, 0, -1, 3] [15, 10, 10, 10]' | ./gusdl
17 回で収束しました.
解: [5.0, 5.0, 5.0, 5.0]
```
## クレジット
### 使用ライブラリ
- **Python標準ライブラリ**
    - [sys](https://docs.python.org/ja/3/library/sys.html) 
### 参考
- [Pythonのeval関数について現役エンジニアが解説【初心者向け】](https://magazine.techacademy.jp/magazine/40662) - *テックアカデミーマガジン*
- [【Python入門】stripメソッドで文字を削除しよう](https://www.sejuku.net/blog/50412) - *侍テック編集部*
- [pythonでヤコビ法[Jacobi]とガウス・ザイデル法[Gauss-Seidel ]（反復法）](https://qiita.com/murakamixi/items/61dbea027db3f33d5b41) - *Kazutaka Murakami*
- [sys --- システム固有のパラメーターと関数](https://docs.python.org/ja/3/library/sys.html) - *Python 3.13.0 ドキュメント
- [【Python】最初、混同してしまう「assert, except, raise」文について](https://qiita.com/baby-0105/items/0e30348589fa0a9d2424) - *b*
- [標準入出力のリダイレクト](https://qiita.com/r18j21/items/0e7d0e48c02d14ed9893) - *r18j21*
- [Markdown記法 サンプル集](https://qiita.com/tbpgr/items/989c6badefff69377da7) - *てぃー びー*
- [[5分でマスター]初心者はまずREADMEを書け[テンプレート付き]](https://qiita.com/Canard_engineer_c_cpp/items/81ce4e53881138dbf37f) - *Canard*

## 貢献
このプロジェクトへの貢献は大歓迎です 。 
バグ報告や新機能の提案など、どんな形でも構いません。
### 貢献方法
1. このリポジトリをフォークする。(ページ右上のForkからどうぞ)
2. 新しいブランチを作成する。
3. コードをコミットする。
4. プッシュする。
5. プルリクエストを作成する。(Contribute → Open pull request)
　
## ライセンス
- このソフトウェアパッケージは，[3条項BSDライセンス](LICENSE)の下，再頒布および使用が許可されます。
- © 2024 Yusei Kobayashi
