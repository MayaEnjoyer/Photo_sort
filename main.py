import os
import shutil
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime


source_folder = "C:\\Users\\Мах\\Desktop\\Saved Pictures"
destination_folder = "C:\\Users\\Мах\\Desktop\\Saved photos by date"



def get_date(photo_path):
    try:
        image = Image.open(photo_path)
        exif_data = image._getexif()
        if exif_data:
            for tag, value in exif_data.items():
                if TAGS.get(tag) == "DateTimeOriginal":
                    return value.split(' ')[0].replace(':', '-')
    except Exception as e:
        print(f"Error reading EXIF for {photo_path}: {e}")

    try:
        creation_time = os.path.getctime(photo_path)
        return datetime.fromtimestamp(creation_time).strftime("%Y-%m-%d")
    except Exception as e:
        print(f"Error getting creation date for {photo_path}: {e}")
        return 'unknown'


def sort_photos():
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        if os.path.isfile(file_path) and filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            date_folder_name = get_date(file_path)

            date_folder = os.path.join(destination_folder, date_folder_name)
            os.makedirs(date_folder, exist_ok=True)

            shutil.move(file_path, os.path.join(date_folder, filename))
            print(f"{filename} → {date_folder}")

sort_photos()
