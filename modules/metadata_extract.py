from PIL import Image
from PIL.ExifTags import TAGS
from core.utils import *

def run():
    title()
    path = input("[$] Enter image path: ")
    try:
        img = Image.open(path)
        exif = img._getexif()
        for tag_id, val in exif.items():
            tag = TAGS.get(tag_id, tag_id)
            printOk(f"{tag}: {val}")
    except Exception as e:
        printNotOk(str(e))
    pause()
