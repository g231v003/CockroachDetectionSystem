# 画像を使った検出スクリプト

from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt

# YOLOのモデルをロード
# モデルは次の順で推定の複雑度（より高度な推定が行えるか）が変わります。n → s → m → l → x
# 現在使えるバージョン（以下のコメントアウトを一つ外して使ってください。）: cockroach-n, cockroach-s
#--------------------------------------------------

# model = YOLO("use/cockroach-n.pt")
model = YOLO("use/cockroach-s.pt") 

#--------------------------------------------------

# 画像の読み込み
image_path = r"ここに画像のパスを入力"
image = cv2.imread(image_path)

# 物体検知の実行
results = model(image)

# 検出結果を画像に描画
annotated_image = results[0].plot()

# 検出結果を表示
plt.imshow(cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
