import cv2

def overlay_image(base_image_path, overlay_image_path, x, y, width, height, output_path):
    """
    画像Aに画像Bを指定した範囲に貼り付ける関数。

    Args:
        base_image_path (str): 背景となる画像Aのパス。
        overlay_image_path (str): 貼り付ける画像Bのパス。
        x (int): 貼り付け先の左上のx座標。
        y (int): 貼り付け先の左上のy座標。
        width (int): 貼り付け範囲の幅。
        height (int): 貼り付け範囲の高さ。
        output_path (str): 出力画像の保存先パス。
    """
    # 画像の読み込み
    base_image = cv2.imread(base_image_path)
    overlay_image = cv2.imread(overlay_image_path)

    if base_image is None:
        print(f"背景画像 {base_image_path} を読み込めませんでした。")
        return
    if overlay_image is None:
        print(f"貼り付け画像 {overlay_image_path} を読み込めませんでした。")
        return

    # 画像Bをリサイズ
    if width < height:
        overlay_image = cv2.rotate(overlay_image, cv2.ROTATE_90_COUNTERCLOCKWISE)

    resized_overlay = cv2.resize(overlay_image, (width, height))

    # 貼り付け範囲の指定
    end_x = x + width
    end_y = y + height

    # 貼り付け範囲を背景画像に合成
    base_image[y:end_y, x:end_x] = resized_overlay

    # 結果を保存
    cv2.imwrite(output_path, base_image)
    print(f"結果を {output_path} に保存しました。")

# 使用例
"""
base_image_path = "imageA.jpg"  # 背景画像Aのパス
overlay_image_path = "imageB.jpg"  # 貼り付ける画像Bのパス
x, y = 50, 100  # 貼り付け先の左上座標
width, height = 200, 150  # 貼り付け範囲の幅と高さ
output_path = "output.jpg"  # 出力画像の保存先

overlay_image(base_image_path, overlay_image_path, x, y, width, height, output_path)

"""
