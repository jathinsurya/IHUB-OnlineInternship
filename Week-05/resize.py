from PIL import Image
import os

def resize_images(input_folder, output_folder, width=384):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            img_path = os.path.join(input_folder, filename)

            img = Image.open(img_path)

            w_percent = width / float(img.size[0])
            height = int(float(img.size[1]) * w_percent)

            img = img.resize((width, height))

            output_path = os.path.join(output_folder, filename)
            img.save(output_path)

            print(f"Resized: {filename}")

resize_images(
    "dataset/images/train",
    "resized/train"
)

resize_images(
    "dataset/images/val",
    "resized/val"
)

resize_images(
    "dataset/images/test",
    "resized/test"
)

print("All images resized successfully!")