# dir_space
[![test](https://github.com/KobayashiYusei/dir_space/actions/workflows/test.yml/badge.svg)](https://github.com/KobayashiYusei/dir_space/actions/workflows/test.yml)
[![GitHub License](https://img.shields.io/github/license/KobayashiYusei/numberGuesser)](LICENSE)
![ROS 2](https://img.shields.io/badge/ROS%202-Jazzy-green)
<img src="https://img.shields.io/badge/ -Python-F9DC3E.svg?logo=python">
-ROS2で任意のファイルシステムの空き容量をパブリッシュするパッケージです。

## 概要
- `pub_node`に任意のファイルシステムのパスを渡すとその場所の空き容量を`dir_space`トピックに流す機能を持ちます。

## 対応環境
- **ROS 2**
    - ROS 2 Jazzy
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
$ ros2 run dir_space pub_node {任意のパス}
```
- 空き容量を調べたいファイルシステムがマウントされているディレクトリのパスをコマンドの末尾に入力して実行します。
- 入力されたパスの空き容量が浮動小数点型でトピックに流れます。単位はGBです。
- パスが存在しない場合パブリッシャは終了します。
- パスを入力しないで実行するとルートディレクトリにマウントされているファイルシステムの空き容量がトピックに流れます。

### 実行例
```bash
$ ros2 run dir_space pub_node /mnt/wsl
[INFO] [1736004774.940271865] [disk_space]: Publish disk space of /mnt/wsl
```
### 出力確認
```bash
$ ros2 topic echo /dir_space
data: 3.792560577392578
```
## クレジット
### 使用したライブラリ・パッケージ
- **Pythonライブラリ**
    - [sys](https://docs.python.org/ja/3/library/sys.html)
    -[rclpy] 
    -[os]
    -[shutil]
    -[sys]
    -[setuptools]
- **ROS2 パッケージ**
    -[std_msgs]
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
