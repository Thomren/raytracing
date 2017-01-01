# -*- coding: utf-8 -*-
from intersection import *
from light import *
from camera import *
from numpy import linalg as la
import numpy as np


def trace_ray(ray, scene):
    """Return the color of the first intersection encountered by ray in
    scene"""
    dmin = -1
    imin = None
    for obj in scene.objects:
        i = intersect(obj, ray)
        if i is not None:
            d = la.norm(i.position - ray.starting_point)
            if imin is None or d < dmin:
                imin = i
                dmin = d
    if imin is not None:
        color = phong_illuminate(scene, imin, ray.starting_point)
    else:
        color = [0., 0., 0.]
    np.clip(color, 0., 1.)
    return color


def raytracer_render(camera, scene):
    """Return a tab representing the rendered image of scene from camera"""
    nrows = camera.image_nrows
    ncols = camera.image_ncols
    res = np.zeros((nrows, ncols, 3))
    for i in range(nrows):
        for j in range(ncols):
            r = camera.ray_at(i, j)
            res[i, j] = trace_ray(r, scene)
    return res
