import os

# アノテーションディレクトリのパスを設定
annotations_dir = "C:/Users/g231v003/Documents/VSCode/project-G/new_datasets/test/labels"

# クラスIDの上限を設定
max_class_id = 0  # nc - 1 に相当

# すべてのアノテーションファイルを処理
for file_name in os.listdir(annotations_dir):
    file_path = os.path.join(annotations_dir, file_name)
    if file_path.endswith(".txt"):
        with open(file_path, "r") as f:
            lines = f.readlines()

        corrected_lines = []
        for line in lines:
            parts = line.strip().split()
            class_id = int(parts[0])

            # クラスIDが上限を超えている場合は修正
            if class_id > max_class_id:
                print(f"修正: {file_name} 内のクラスID {class_id} -> 0")
                parts[0] = "0"

            corrected_lines.append(" ".join(parts))

        # 修正結果を保存
        with open(file_path, "w") as f:
            f.write("\n".join(corrected_lines))
