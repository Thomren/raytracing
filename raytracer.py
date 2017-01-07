# -*- coding: utf-8 -*-
from intersection import *
from light import *
from camera import *
from numpy import linalg as la
import numpy as np
import multiprocessing as mp


def trace_ray(ray, scene, n=10):
    """Return the color of ray after up to n reflexions in scene"""
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
        color = np.clip(color, 0., 1.)
        if n > 0:
            r = imin.object.material.reflection
            indir = ray.direction
            refldir = indir - 2 * (indir.dot(imin.normal)) * imin.normal
            reflected = Ray(imin.position, refldir)
            return color * (1 - r) + trace_ray(reflected, scene, n - 1) * r
    else:
        color = np.array([0., 0., 0.])
    return color

def pixel_render(i, j, camera, scene):
        r = camera.ray_at(i, j)
        return trace_ray(r, scene)

def raytracer_render(camera, scene):
    """Return a tab representing the rendered image of scene from camera"""
    nrows = camera.image_nrows
    ncols = camera.image_ncols
    res = np.zeros((nrows, ncols, 3))
    pool = mp.Pool()
    for i in range(nrows):
        res[i, :, :] = pool.starmap(pixel_render, [(i, j, camera, scene) for j in range(ncols)])
    pool.close()
    return res
