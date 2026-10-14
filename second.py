import os
from PIL import Image


def batch_convert_to_gray(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".tiff")):
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)
            gray = img.convert("L")
            save_path = os.path.join(output_folder, f"gray_{filename}")
            gray.save(save_path)
            print(f"已轉換: {filename} → {save_path}")


def observe_pixels(image_path, points):
    img = Image.open(image_path)
    for p in points:
        pixel = img.getpixel(p)
        print(f"座標 {p} 的像素值: {pixel}")


input_folder = "image"
output_folder = "gray_images"
batch_convert_to_gray(input_folder, output_folder)


observe_pixels("image/smaple.jpg", [(0,0), (50,50), (100,100)])
