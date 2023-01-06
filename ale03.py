### chap06/ale03.py: Build a simple image containing a checkerboard
from PIL import Image

# Width and height of our image
sz = (100, 100)

# Create a single plane of black and white pixels, initialized to black
im = Image.new('L', sz)

# Create direct access to the pixels in the image
pixels = im.load()

# Set the color of each pixel
for i in range(sz[0]):
    for j in range(sz[1]):
        # Creates a checkerboard
        pixels[i,j] = 255

im.save('images/ale03.png')
# im.show()   # Feel free to use if you're running locally
