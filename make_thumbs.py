import os
from PIL import Image

# Folders:
folders = [
    "AD",
    "INDIA",
    "NIMMA",
    "ART",
    "BIRDS",
    "COLOMBIA",
    "LANDSCAPE",
    "AMAZON",
    "CATS",
    "GALAPAGOS",
    "ME"
]

THUMB_SIZE = (500, 500)  # adjust if you like

for folder in folders:
    thumbs_dir = os.path.join(folder, "thumbs")
    os.makedirs(thumbs_dir, exist_ok=True)

    for filename in os.listdir(folder):
        full_path = os.path.join(folder, filename)

        # Skip non-images and skip directories
        if not os.path.isfile(full_path):
            continue
        if filename.lower().endswith(".json"):
            continue

        # Skip if thumbnail already exists
        thumb_path = os.path.join(thumbs_dir, filename)
        if os.path.exists(thumb_path):
            continue

        try:
            img = Image.open(full_path)
            img.thumbnail(THUMB_SIZE)
            img.save(thumb_path, "JPEG", quality=85)
            print(f"Created: {thumb_path}")
        except Exception as e:
            print(f"Error processing {full_path}: {e}")
