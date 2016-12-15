# Show to python where to find the Camera module
import sys
sys.path.append('..')

from scene import *
from light import *
from intersection import *
import numpy as np
from numpy import linalg as la

s = Sphere([0,0,3], 1, Material(np.array([0.1,0.2,0.3]), 0., 0.2, 0.3, 0.4, 0.5));
n = np.array([0,0,-1])
l = Spotlight([0,0,0], np.array([0,0,1]));
p = np.array([0,0,2])
v = np.array([0,0,0])

scene1=Scene()
scene1.add_light(l)
i1=Intersection(p, n, s);
print(phong_illuminate(scene1, i1, v))
assert(np.array_equal(phong_illuminate(scene1, i1, v), [0,0,0.15]))

s = Sphere([0,0,3], 1, Material(np.array([0.1,0.2,0.3]), 0., 0.2, 0.3, 0.4, 0.5));
n = np.array([0,0,-1])
l = Spotlight([1,1,0], np.array([0,0,1]));
p = np.array([0,0,2])
v = np.array([0,0,0])

scene2=Scene()
scene2.add_light(l)
i2=Intersection(p, n, s);
assert(la.norm(phong_illuminate(scene2, i2, v) - np.array([0, 0, 0.13])) < 0.01)


s = Sphere([0,0,3], 1, Material(np.array([0.1,0.2,0.3]), 0., 0.2, 0.3, 0.4, 0.5));
n = np.array([0,0,-1])
l = Spotlight([0,0,10], np.array([0,0,1]));
p = np.array([0,0,2])
v = np.array([0,0,0])


scene3=Scene()
scene2.add_light(l)
i3=Intersection(p, n, s);
assert(np.array_equal(phong_illuminate(scene3, i3, v), [0,0,0]))
