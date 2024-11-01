# ゴキブリ検知システム

## 概要
YOLO11(https://docs.ultralytics.com/models/yolo11/) を使用して、ゴキブリの検知を行います。

学習用のプログラムも用意しました。

## 実行環境・必要なライブラリ
Python - 3.10.12

### 必須ライブラリ

・ultralytics
```console
pip install ultralytics
```

### 学習に必要なライブラリ

・pytorch

PyTorch公式（https://pytorch.org/get-started/previous-versions/） を参照してインストールしてください。

## 使い方
### 実行可能なファイル
・test.py - カメラからリアルタイムでゴキブリを検知するプログラム

・test2.py - 画像を参照してゴキブリを検知するプログラム

・lrean.py - 学習用プログラム

・GPU-check.py - 学習時にGPUを使用できるかチェックするプログラム

詳しい使い方は各ファイルに記載
