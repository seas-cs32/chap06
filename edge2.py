### chap06/edge2.py
from PIL import Image

# Width and height of our image
sz = (400, 400)

# Create a single plane of black and white pixels, initialized to black
im = Image.new('L', sz)

# Create direct access to the pixels in the image
pixels = im.load()

# Set the color of each pixel
for i in range(sz[0]):
    for j in range(sz[1]):
        # Creates a diagonal fade
        pixels[i,j] = i + j

im.save('images/out.png')

#print(pixels[399, 399])

#pixels[399, 399] = -1
#print(pixels[399, 399])
