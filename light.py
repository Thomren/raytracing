# -*- coding: utf-8 -*-
from ray import *
from intersection import *
from light import *
import numpy as np
from numpy import linalg as la


class Spotlight:

    def __init__(self, position, color):
        self.position = position
        self.color = color


def normalize(vect):
    """Normalize the vector vect"""
    if la.norm(vect):
        return vect / la.norm(vect)
    else:
        return vect


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
    i = [0.] * nblights  # stores the illuminations calculated for each light
    res = np.array([float(ka)] * 3)
    for k in range(nblights):
        if n.dot(l[k]) > 0 and not shadow_test(scene.lights[k],
                                               scene, intersection):
            i[k] += kd * l[k].dot(n) + ks * (max(0, r[k].dot(v)))**alpha
            res += i[k] * scene.lights[k].color
    return res * m.color


def shadow_test(light, scene, intersection):
    """Return True if the intersection if hidden by another object, False
    else"""
    pi = intersection.position
    pl = light.position
    ray = Ray(intersection.position, pl - pi)
    for obj in scene.objects:
        if obj != intersection.object:
            i = intersect(obj, ray)
            if i is not None and la.norm(i.position - pi) < la.norm(pl - pi):
                return True
    return False
