# -*- coding: utf-8 -*-
from intersection import *
from light import *
from camera import *
from numpy import linalg as la
import numpy as np
import multiprocessing as mp


def trace_ray(ray, scene, n=20, clip=True):
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
        r = imin.object.material.reflection
        if n > 0:
            indir = ray.direction
            refldir = indir - 2 * (indir.dot(imin.normal)) * imin.normal
            reflected = Ray(imin.position, refldir)
            res = color * (1 - r) + trace_ray(reflected,
                                              scene, n - 1, False) * r
            if clip:
                res = np.clip(res, 0., 1.)
            return res
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
    # Calculate the rendered pixels using multiprocessing and pixel_render
    res = np.reshape(pool.starmap(pixel_render, [(i, j, camera, scene) for i in range(nrows) for j in range(ncols)]), (nrows, ncols, 3))
    pool.close()
    return res
