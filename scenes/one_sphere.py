# -*- coding: utf-8 -*-
import sys
sys.path.append('..')

from scene import *
from camera import *
from light import *
from raytracer import *
import numpy as np
import matplotlib.image as mpli

s = Sphere([0,0,3], 2, Material(np.array([0,0,1]), 0, 0.2, 0.3, 0.4, 0.5))
l = Spotlight([1,1,0], np.array([1,1,1]))
scene = Scene()
scene.add_light(l)
scene.add_object(s)
camera = Camera(200,200,1)

picture = raytracer_render(camera, scene)
mpli.imsave("one_sphere.png",picture)