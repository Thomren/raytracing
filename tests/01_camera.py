# Show to python where to find the Camera module
import sys
sys.path.append('..')

# Import the Camera module
from camera import *

# Instantiate a Camera object
c = Camera(100, 200, 3)

# Test its members
assert(c.image_nrows == 100)
assert(c.image_ncols == 200)
assert(c.focal_length == 3)
