import cv2
import matplotlib.pyplot as plt
from ultralytics import YOLO  # YOLOv8などに応じて変更
import os  # ファイルパス操作に必要
def detect_and_save_objects(image_path, model_path="use\cockroach-s.pt"):
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

    # 推論結果から信頼度スコアを抽出
    confidence_scores = []  # 信頼度スコアを格納するリスト
    for result in results:  # 結果の各検出についてループ
        boxes = result.boxes.cpu().numpy()  # 推論結果を取得
        for box in boxes:
            confidence = box.conf  # 信頼度スコアを取得
            confidence_scores.append(confidence)  # リストに追加
    scores_list = [float(score[0]) for score in confidence_scores]
    max_score = max(scores_list)
    
    # 信頼度スコアを確認
    print(max_score)

    # 検出結果を画像に描画
    annotated_image = results[0].plot()  # YOLOv5の結果描画機能を利用
    # 保存パスを決定（入力画像と同じディレクトリに保存）
    input_dir = os.path.dirname(image_path)
    output_path = os.path.join(input_dir, "annotated_image.jpg")
    # 検出結果を保存
    cv2.imwrite(output_path, annotated_image)
    print(f"検出結果の画像を {output_path} に保存しました。")
    # 検出結果を表示
    # plt.imshow(cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB))
    # plt.axis("off")
    # plt.show()

    return(max_score)
# 使用例
input_image_path = r"inout_image\capture.jpg"
detect_and_save_objects(input_image_path)