import os
from PIL import Image

def batch_resize(input_folder, output_folder, size=(300, 200)):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".tiff")):
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)
            resized = img.resize(size)
            save_path = os.path.join(output_folder, f"resized_{filename}")
            resized.save(save_path)
            print(f"已縮放: {filename} → {save_path}, 尺寸: {resized.size}")


input_folder = "image"
output_folder = "resized_images"
batch_resize(input_folder, output_folder, size=(300, 200))
