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
s0 = Sphere([0, 1, 3], 0.5, Material(
    np.array([1, 1, 0]), 0.1, 0.8, 0.8, 10, 0.4))
s1 = Sphere([0, -1, 3], 0.5, Material(
    np.array([0, 0, 1]), 0.1, 0.8, 0.8, 10, 0.4))
s2 = Sphere([1, 0, 3], 0.5, Material(
    np.array([1, 0, 0]), 0.1, 0.8, 0.8, 10, 0.4))
s3 = Sphere([-1, 0, 3], 0.5, Material(
    np.array([0, 1, 0]), 0.1, 0.8, 0.8, 10, 0.4))
s = Sphere([0, 0, 15], 10, Material(
    np.array([0.8, 0.8, 0.8]), 0.2, 0.8, 0.8, 10, 0.4))
sl = Sphere([0, 0, 3], 0.3, Material(
    np.array([1, 0, 0.5]), 0.2, 0.8, 0.8, 10, 0.4))
t = Triangle([0, 5, 50], [-30, -2, -1], [30, -2, -1], Material(
    np.array([0.3, 0.5, 0.8]), 0.1, 0.9, 0.9, 5, 0.2))
# Definition of the lights
l = Spotlight(np.array([1, 1, 0]), np.array([0.5, 0.5, 0.5]))
l1 = Spotlight(np.array([-1, 1, 0]), np.array([0.5, 0.5, 0.5]))
l2 = Spotlight(np.array([0, 1, 0]), np.array([0.3, 0.3, 0.3]))
# Creation of the scene
scene = Scene()
scene.add_light(l)
scene.add_light(l1)
scene.add_light(l2)
scene.add_object(s3)
scene.add_object(s2)
scene.add_object(s1)
scene.add_object(s0)
scene.add_object(s)
scene.add_object(sl)

scene.add_object(t)
# Creation of the camera
camera = Camera(500, 500, 1)

# Rendering
if __name__ == "__main__":
    print('Rendering in progress')
    picture = raytracer_render(camera, scene)
    print('Saving the image')
    mpli.imsave("examplewithoutspec.png", picture)
    print('Image saved')
