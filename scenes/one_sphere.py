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
s = Sphere([0, 0, 3], 1, Material(
    np.array([0, 0, 1]), 0.4, 0.2, 0.8, 10, 0))
# Definition of the lights
l = Spotlight([1, 1, 0], np.array([1, 1, 1]))
# Creation of the scene
scene = Scene()
scene.add_light(l)
scene.add_object(s)
# Creation of the camera
camera = Camera(200, 200, 1)
if __name__ == "__main__":
    # Rendering
    print('Rendering in progress')
    picture = raytracer_render(camera, scene)
    print('Saving the image')
    mpli.imsave("testthomasmoi.png", picture)
    print('Image saved')
