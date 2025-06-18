import os
import time
from PIL import Image

# Paths based on your structure
INPUT_FOLDER = os.path.join(os.path.dirname(__file__), "raw-images")
OUTPUT_FOLDER = os.path.join(os.path.dirname(__file__), "compressed-images")
COMPRESSION_QUALITY = 30  # JPEG quality: 0 (worst) to 100 (best)

def compress_image(image_path, output_folder):
    try:
        img = Image.open(image_path)
        filename = os.path.basename(image_path)
        name, _ = os.path.splitext(filename)
        output_path = os.path.join(output_folder, f"{name}_compressed.jpg")
        img = img.convert("RGB")  # Ensure JPEG compatibility
        img.save(output_path, "JPEG", quality=COMPRESSION_QUALITY)
        print(f"Compressed: {filename}")
    except Exception as e:
        print(f"Failed to compress {image_path}: {e}")

def main():
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    image_files = [
        os.path.join(INPUT_FOLDER, f)
        for f in os.listdir(INPUT_FOLDER)
        if f.lower().endswith((".png", ".jpg", ".jpeg"))
    ]

    total = len(image_files)
    print(f"Found {total} image(s) to compress.")
    start_time = time.time()

    for image_file in image_files:
        compress_image(image_file, OUTPUT_FOLDER)

    end_time = time.time()
    duration = end_time - start_time
    print(f"\nSequential compression completed in {duration:.2f} seconds")
    print(f"Total images processed: {total}")

if __name__ == "__main__":
    main()
