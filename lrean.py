# 学習用スクリプト
# 学習データを追加する際は、次の割合で「detasets」フォルダ内に画像とアノテーションデータを入れてください。
# トレーニングデータ (train)：70～80％
# 検証データ (val)：10～15％
# テストデータ (test)：10～15％

from ultralytics import YOLO

if __name__ == '__main__':
    # YOLOモデルの読み込み（事前学習済みモデル）
    # 注意：学習には相当な時間がかかります。事前学習済みモデルは基本的に「yolo11n.pt」を使用してください。

    model = YOLO("yolo11n.pt")
    # model = YOLO("yolo11s.pt")
    # model = YOLO("yolo11m.pt")
    # model = YOLO("yolo11l.pt")
    # model = YOLO("yolo11x.pt")

    # トレーニングの実行
    model.train(data="cockroach.yaml", epochs=50, batch=32, project="data_output/runs", device=0) 

    """
    学習完了後、「data_output/runs/train(学習回数)/weights」フォルダ内に二つptファイルが生成されます。
    best.pt: 学習した中で最も良いスコアを出した学習データ
    last.pt: 最後に学習したデータ

    使用する際は、学習時のパスを変更して使ってください。

    例) test.pyで使用する場合
    12行目 model = YOLO("data_output/runs/train/weights/best.pt") 

    もしよさそうな学習データができた場合、slackで教えてもらえると助かります

    """
