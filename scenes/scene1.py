# -*- coding: utf-8 -*-
import sys
sys.path.append('..')


from scene import *
from camera import *
from light import *
from raytracer import *
import numpy as np
import matplotlib.image as mpli

# Definition of the objects
s1 = Sphere([0, 0, 3], 0.8, Material(
    np.array([0, 0, 1]), 0.2, 0.8, 0.8, 30, 0.2))
s2 = Sphere([1, 1, 2], 0.3, Material(
    np.array([1, 0, 0]), 0.2, 0.8, 0.8, 10, 0.1))
t = Triangle([-1, -1, 3], [-2, -1, 3], [-1, -2, 3], Material(
    np.array([1, 1, 0]), 0.1, 0.9, 0.9, 5, 0))
background = Sphere([0, 0, 0], 10, Material(
    np.array([1, 1, 1]), 1, 0, 0, 0, 0))
# Definition of the lights
l = Spotlight(np.array([1, 1, 0]), np.array([1, 1, 1]))
# Creation of the scene
scene = Scene()
scene.add_light(l)
scene.add_object(s1)
scene.add_object(s2)
scene.add_object(background)
scene.add_object(t)
# Creation of the camera
camera = Camera(100, 100, 1)

# Rendering
if __name__ == "__main__":
    print('Rendering in progress')
    picture = raytracer_render(camera, scene)
    print('Saving the image')
    mpli.imsave("reflexionbis.png", picture)
    print('Image saved')
