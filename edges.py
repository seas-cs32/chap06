### chap06/edges.py
from PIL import Image, ImageFilter

imfile = input('Name of imagefile: ')

with Image.open('images/' + imfile) as im:
    # Apply a filter that detects edges
    filtered = im.filter(ImageFilter.CONTOUR)
    filtered.save('images/out.png')
