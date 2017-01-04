# -*- coding: utf-8 -*-
import numpy as np
from numpy import linalg as la


class Spotlight:

    def __init__(self, position, color):
        self.position = position
        self.color = color


def normalize(vect):
    """Normalize the vector vect"""
    return vect / la.norm(vect)


def phong_illuminate(scene, intersection, viewer):
    """Return the intensity of the light at intersection from viewer with the
    Phong reflection model"""
    m = intersection.object.material  # Material of the object
    nblights = len(scene.lights)
    ks, kd, ka, alpha = m.specular, m.diffuse, m.ambiant, m.shininess
    # Constants of specular, diffuse and ambient reflection, and shininess
    # constants
    n = normalize(intersection.normal)
    l = [normalize(scene.lights[i].position -
                   intersection.position) for i in range(nblights)]
    # l contain the direction vectors from the intersection toward each light
    # source
    r = [normalize(2 * (l[i].dot(n)) * n - l[i]) for i in range(nblights)]
    # r contain the directions that a perfectly reflected ray of light would
    # take
    v = normalize(viewer - intersection.position)
    # v is the direction pointing towards the viewer
    i = [ka] * nblights  # stores the illuminations calculated for each light
    res = np.array([0., 0., 0.])
    for k in range(nblights):
        if n.dot(l[k]) > 0:
            diffuse = l[k].dot(n)
            specular = r[k].dot(v)
            if diffuse >= 0:
                i[k] += kd * diffuse
            if specular >= 0:
                i[k] += ks * (specular)**alpha
            res += i[k] * m.color * scene.lights[k].color
    return res
