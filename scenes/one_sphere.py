# -*- coding: utf-8 -*-
import sys
sys.path.append('..')


from scene import *
from camera import *
from light import *
from raytracer import *
import numpy as np
import matplotlib.image as mpli

#Defintion of the objects
s1 = Sphere([0, 0, 3], 2, Material(np.array([0, 0, 1]), 1, 0.2, 0.3, 2, 0.5))
s2 = Sphere([0, 0, 4], 3, Material(np.array([1, 0, 0]), 1, 0.2, 0.3, 2, 0.5))
background = Sphere([0,0,0], 10, Material(np.array([1,1,1]), 1, 0, 0, 0, 0))
#Definition of the lights
l = Spotlight([0, 0, 0], np.array([1, 1, 1]))
#Creation of the scene
scene = Scene()
scene.add_light(l)
scene.add_object(s1)
#scene.add_object(s2)
#Creation of the camera
camera = Camera(200, 200, 1)

#Rendering
print('Rendering in progress')
picture = raytracer_render(camera, scene)
print('Saving the image')
mpli.imsave("one_sphere.png", picture)
print('Image saved')