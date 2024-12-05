import cv2
import matplotlib.pyplot as plt
from ultralytics import YOLO  # YOLOv8などに応じて変更
import os  # ファイルパス操作に必要
import picture_

def detect_and_save_objects(image_path, model_path=r"use\best.pt"):
    """
    画像に対して物体検出を実行し、結果を保存および表示する関数。
    Args:
        image_path (str): 入力画像のパス。
        model_path (str): 使用するYOLOモデルのパス（デフォルト: yolov5s.pt）。
    """
    # モデルのロード
    model = YOLO(model_path)  # 適切なモデルファイルを指定
    # 画像の読み込み
    image = cv2.imread(image_path)
    if image is None:
        print(f"画像を読み込めませんでした: {image_path}")
        return
    # 物体検知の実行
    results = model(image)

    # 座標情報と大きさを配列に格納
    xy = []
    widhigh = []

    # 推論結果から信頼度スコアを抽出
    for result in results:
        boxes = result.boxes.cpu().numpy()  # 推論結果を取得
        for box in boxes:
            # バウンディングボックスの座標とサイズを取得
            x1, y1, x2, y2 = map(float, box.xyxy[0])  # ndarrayをfloatに変換
            xy.append([x1,y1])
            width = x2 - x1  # 幅
            height = y2 - y1  # 高さ
            widhigh.append([width,height])
            confidence = float(box.conf)  # 信頼度スコアをfloatに変換
            print(f"物体検出: 座標=({x1:.1f}, {y1:.1f}), ({x2:.2f}, {y2:.2f}), "
                  f"幅={width:.1f}px, 高さ={height:.1f}px, 信頼度={confidence:.2f}")

    # 検出結果を画像に描画
    annotated_image = results[0].plot()  # YOLOの結果描画機能を利用
    # 保存パスを決定（入力画像と同じディレクトリに保存）
    input_dir = os.path.dirname(image_path)
    output_path = os.path.join(input_dir, "annotated_image.jpg")
    # 検出結果を保存
    cv2.imwrite(output_path, annotated_image)
    print(f"検出結果の画像を {output_path} に保存しました。")

    for i in range(0,len(xy),1):
        picture_.overlay_image(r"inout_image\annotated_image.jpg", r"picture\bug_gokiburi.jpg", int(xy[i][0]), int(xy[i][1]), int(widhigh[i][0]), int(widhigh[i][1]), r"inout_image\annotated_image.jpg")

# 使用例
input_image_path = r"inout_image\capture.jpg"
detect_and_save_objects(input_image_path)
