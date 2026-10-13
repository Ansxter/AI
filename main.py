import os
from PIL import Image

def batch_resize(input_folder, output_folder, size):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".tiff")):
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)
            resized = img.resize(size)
            save_path = os.path.join(output_folder, f"{size[0]}x{size[1]}_{filename}")
            resized.save(save_path)
            print(f"{filename} → {resized.size}, 已輸出到 {save_path}")


input_folder = "image"
output_folder = "resized_image"

batch_resize(input_folder, output_folder, (300, 200))
batch_resize(input_folder, output_folder, (800, 600))
batch_resize(input_folder, output_folder, (150, 150))

