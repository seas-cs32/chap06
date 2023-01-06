### chap06/ale02.py
from PIL import Image

# Width and height of our image
sz = (100, 100)

# Create a single plane of RGB pixels, initialized to black
im = Image.new('L', sz)

# Create direct access to the pixels in the image
pixels = im.load()

# Set the color of each pixel
for i in range(sz[0]):
    for j in range(sz[1]):
        pixels[i,j] = ???

im.save('images/ale02.png')
# im.show()   # Feel free to use if you're running locally
