# dir_space
[![test](https://github.com/KobayashiYusei/dir_space/actions/workflows/test.yml/badge.svg)](https://github.com/KobayashiYusei/dir_space/actions/workflows/test.yml)
[![GitHub License](https://img.shields.io/github/license/KobayashiYusei/numberGuesser)](LICENSE)
![ROS 2](https://img.shields.io/badge/ROS%202-Jazzy-green)
<img src="https://img.shields.io/badge/ -Python-F9DC3E.svg?logo=python">
- ROS2で任意のファイルシステムの空き容量をパブリッシュするパッケージです。

## 概要
- `pub_node`に任意のファイルシステムのパスを渡すとその場所の空き容量を`dir_space`トピックに流す機能を持ちます。

## 対応環境
- **ROS 2**
    - ROS 2 Jazzy
- **OS**
    - Ubuntu 22.04.1 LTS

## 使い方
```bash
$ ros2 run dir_space pub_node {任意のパス}
```
- 空き容量を調べたいファイルシステムがマウントされているディレクトリのパスをコマンドの末尾に入力して実行します。
- 入力されたパスの空き容量の値が浮動小数点型でトピックに流れます。単位はGBです。
- 存在しないパスを入力して実行した場合パブリッシャは終了します。
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
### 使用させていただいたライブラリ・パッケージ
- **Pythonライブラリ**
    - [shutil](https://docs.python.org/3/library/shutil.html)
    - [setuptools](https://setuptools.pypa.io/en/latest/)
- **ROS2パッケージ**
    - [std_msgs](https://docs.ros.org/en/noetic/api/std_msgs/html/index-msg.html)
    - [rclpy](https://docs.ros.org/en/iron/p/rclpy/)

### 使用させていただいたコンテナ
このプロジェクトでは、以下のDockerコンテナを使用しています：
- [ryuichiueda/ubuntu22.04-ros2:latest](https://hub.docker.com/r/ryuichiueda/ubuntu22.04-ros2)  - *ryuichiueda*
### 参考
- [std_msgs Msg/Srv Documentation](https://docs.ros.org/en/noetic/api/std_msgs/html/index-msg.html) - *ROS Wiki*
- [Pythonでディレクトリごとのディスク使用容量を一覧化する](https://qiita.com/estaro/items/c298d3c1b2a39e0f4336) - *estaro*
- [[Python]コマンドライン引数を受け取る方法](https://qiita.com/to-fmak/items/4b136479099826959ea6) - *Wenzhang*
- [bashでのPID取得方法まとめ($$、$PPID、$!、$BASHPID)](https://qiita.com/laikuaut/items/1daa06900ad045d119b4) - *Shota*
- [Throw exception ExternalShutdownException while receiving signal SIGTERM #841](https://github.com/ros2/rclpy/issues/841) - *Barry-Xu-2018 *
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
- © 2025 Yusei Kobayashi
