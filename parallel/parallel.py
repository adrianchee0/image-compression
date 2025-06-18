import os
import time
from PIL import Image
from concurrent.futures import ProcessPoolExecutor

INPUT_FOLDER = os.path.join(os.path.dirname(__file__), "raw-images")
OUTPUT_FOLDER = os.path.join(os.path.dirname(__file__), "compressed-images")
COMPRESSION_QUALITY = 30  # Adjust as needed

def compress_image(image_file):
    try:
        image_path = os.path.join(INPUT_FOLDER, image_file)
        img = Image.open(image_path)
        name, _ = os.path.splitext(image_file)
        output_path = os.path.join(OUTPUT_FOLDER, f"{name}_compressed.jpg")
        img = img.convert("RGB")
        img.save(output_path, "JPEG", quality=COMPRESSION_QUALITY)
        print(f"Compressed: {image_file}")
    except Exception as e:
        print(f"Failed to compress {image_file}: {e}")

def main():
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    image_files = [
        f for f in os.listdir(INPUT_FOLDER)
        if f.lower().endswith((".png", ".jpg", ".jpeg"))
    ]

    total = len(image_files)
    print(f"Found {total} image(s) to compress.")
    start_time = time.time()

    with ProcessPoolExecutor() as executor:
        executor.map(compress_image, image_files)

    end_time = time.time()
    duration = end_time - start_time
    print(f"\nParallel compression completed in {duration:.2f} seconds")
    print(f"Total images processed: {total}")

if __name__ == "__main__":
    main()
