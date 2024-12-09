# カメラを使った検出スクリプト

import cv2
from ultralytics import YOLO

# YOLOのモデルをロード
# モデルは次の順で推定の複雑度（より高度な推定が行えるか）が変わります。n → s → m → l → x
# 現在使えるバージョン（以下のコメントアウトを一つ外して使ってください。）: cockroach-n, cockroach-s
#--------------------------------------------------

# model = YOLO("use/cockroach-n.pt")
model = YOLO("use/cockroach-sv2.pt") 

#--------------------------------------------------

# Webカメラの起動
# VideoCaptureの引数は、0 → デフォルトカメラ,　1以降の数 → サブカメラや外部カメラ　になります。
#--------------------------------------------------

cap = cv2.VideoCapture(1)

#--------------------------------------------------

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # YOLOで物体検出を行う
    results = model(frame, conf=0.55)

    # 検出された物体の数を取得
    num_objects = len(results[0].boxes)  # 検出されたボックスの数をカウント

    # 検出結果をフレームに描画
    g_sum = results[0].plot()

    # 検出された物体の数を画像に表示
    cv2.putText(g_sum, f"G-sum: {num_objects}", (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

    # ウィンドウに描画した結果を表示
    cv2.imshow("YOLO Detection", g_sum)

    # 'q'を押すと終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
