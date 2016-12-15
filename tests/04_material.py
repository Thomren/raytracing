import sys
sys.path.append('..')

from scene import *
import numpy as np

m = Material([0,0,1], 0.1, 0.2, 0.3, 0.4, 0.5);

assert(np.array_equal(m.color, np.array([0,0,1])))
assert(m.ambiant == 0.1)
assert(m.diffuse == 0.2)
assert(m.specular == 0.3)
assert(m.shininess == 0.4)
assert(m.reflection == 0.5)
