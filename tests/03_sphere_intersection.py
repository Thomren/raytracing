# Show to python where to find the modules
import sys
sys.path.append('..')

import numpy as np
from numpy import linalg as la

from scene import *
from camera import *
from intersection import *

def is_parallel(v1, v2):
    return ((v1.dot(v2) / (la.norm(v1) * la.norm(v2))) - 1.) < 0.01

s = Sphere(np.array([0,0,3]), 1, Material(np.array([0,0,1.]), 1, 1, 1, 1, 1))
print(type(s))

r = Ray(np.array([0,0,0]), np.array([0,0,1]))
i = intersect(s, r)
assert np.array_equal(i.position, np.array([0,0,2.])), "Error with a ray starting outside the sphere."
assert is_parallel(i.normal, np.array([0,0,-1.])), "Error with the normal of a ray starting outside the sphere."

r = Ray(np.array([0,0,10]), np.array([0,0,-1]))
i = intersect(s, r)
assert np.array_equal(i.position, np.array([0,0,4.])), "Error with a ray starting outside the sphere."
assert is_parallel(i.normal, np.array([0,0,1.])), "Error with the normal of a ray starting outside the sphere."

r = Ray(np.array([0,0,3]), np.array([0,0,-1]))
i = intersect(s, r)
assert np.array_equal(i.position, np.array([0,0,2.])), "Error with a ray starting inside the sphere."
assert is_parallel(i.normal, np.array([0,0,1.])), "Error with the normal of a ray starting inside the sphere."

r = Ray(np.array([0,0,5]), np.array([0,0,1]))
i = intersect(s, r)
assert i is None, "Error with a ray not intersecting the sphere: intersect should return None."
