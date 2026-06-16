from PIL import Image
import os
import glob

# 変換したいフォルダのパス
input_dir = "./input"
output_dir = os.path.join(input_dir, "output")

os.makedirs(output_dir, exist_ok=True)

# JPG/JPEG をすべて取得
for file in glob.glob(os.path.join(input_dir, "*.jpg")) + glob.glob(os.path.join(input_dir, "*.jpeg")):
    img = Image.open(file)
    base = os.path.splitext(os.path.basename(file))[0]

    output_path = os.path.join(output_dir, base + ".png")

    # 速度優先（圧縮しない）
    img.save(output_path, "PNG", optimize=False, compress_level=0)

    print(f"変換完了: {output_path}")
