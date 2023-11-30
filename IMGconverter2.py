#Author:   Duncan McEwan
#Date:     11/13/2023
#Purpose:  Convert 99 ULS testing .HEIC image files to jpg so that when we send
#          Archer the test report, they can open a more unniversal
#          photo file format and so that I don't have to convert them by hand

from PIL import Image
import os
from pillow_heif import register_heif_opener

register_heif_opener()

heic_files = [photo for photo in os.listdir() if '.HEIC' in photo]

for photo in heic_files:
    temp_img = Image.open(photo)
    jpg_photo = photo.replace('.HEIC','.JPG')
    temp_img.save(jpg_photo)