### chap06/ale05.py
import sys
from PIL import Image

# Check for proper usage and grab the image filename
if len(sys.argv) == 1:
    imfile = 'images/' + input('Filename of image: ')
elif len(sys.argv) == 2:
    imfile = 'images/' + sys.argv[1]
else:
    sys.exit("Usage: python3 ale05.py imagefile")

with Image.open(imfile) as im:
    # Apply a filter that enhances the red and desaturates blue/green
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            r, g, b = im.getpixel((x,y))
            im.putpixel((x,y), (r, g//50, b//50))

    im.save('images/ale05.png')
