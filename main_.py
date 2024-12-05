import RPi.GPIO as GPIO
import time
import requests
import subprocess
import os
import datetime
import image_detection

# LINE Notifyのアクセストークン
LINE_NOTIFY_TOKEN = '7CPebnn88I1Q0Buf5pb6IgccVHHUSXXakiEY4qgnOaQ'  # あなたのトークンに置き換えてください
LINE_NOTIFY_API = 'https://notify-api.line.me/api/notify'

# PIRセンサーのGPIOピン番号（例としてGPIO 26）
PIR_PIN = 26

# 変数
percent = 0
place = "冷蔵庫"
dt_now = datetime.datetime.now()

# GPIOの設定
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

# 写真を撮影する関数
def capture_image():
    # 保存先フォルダ
    save_directory = "inout_image"
    # 保存するファイル名
    filename = "capture.jpg"
    # 保存する完全なパス
    full_path = os.path.join(save_directory, filename)

    # フォルダがなければ作成
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)
        print(f"保存先フォルダを作成しました: {save_directory}")
    
    # 写真を撮影
    subprocess.run(["fswebcam", "-r", "1280x720", "--no-banner", full_path])
    print(f"写真を保存しました: {full_path}")
    return full_path

# LINEに写真を送信する関数
def send_image_to_line(filename):
    headers = {'Authorization': f'Bearer {LINE_NOTIFY_TOKEN}'}
    payload = {'message': '人感センサーが反応しました！'+ 
                   dt_now.strftime('\n\n%Y年%m月%d日 %H:%M:%S') + 
                   f"\nゴキブリ確率{percent}％" + 
                   f"\n{place}付近にてゴキブリらしき物体を確認" + 
                   "\n発見しても冷静に対応しよう。" + 
                   "\nゴキブリ対処法はこちら" + 
                   "\nhttps://x.gd/Gokiburitaisaku"}
    files = {'imageFile': open(filename, 'rb')}

    response = requests.post(LINE_NOTIFY_API, headers=headers, data=payload, files=files)
    if response.status_code == 200:
        print("LINEに写真が送信されました")
    else:
        print(f"エラーが発生しました: {response.status_code}")

# メイン処理
try:
    print("人感センサーの監視を開始します...")

    while True:
        # PIRセンサーが反応した場合
        if GPIO.input(PIR_PIN) == GPIO.HIGH:
            reaction_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print("人感センサーが反応しました！" + reaction_time)
            
            # 写真を撮影
            photo_path = capture_image()
            image_detection.detect_and_save_objects()

            # percentが50以上の場合のみLINEを送信
            if percent >= 75:
                print("percentが75以上のため、写真を撮影して送信します...")
                
                # 少し待ってから（撮影が完了するのを待つため）
                time.sleep(2)
                
                # LINEに送信
                send_image_to_line(photo_path)
            
            # 次の検出まで少し待機
            time.sleep(10)  # 人が立ち去るまでの間隔を空ける
        else:
            time.sleep(1)  # センサーが反応していないときは1秒ごとに確認

except KeyboardInterrupt:
    print("プログラムを終了します")

finally:
    GPIO.cleanup()




