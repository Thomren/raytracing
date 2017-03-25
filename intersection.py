# -*- coding: utf-8 -*-
import numpy as np
from numpy import linalg as la
from scene import *


def normalize(vect):
    """Normalize the vector vect"""
    return vect / la.norm(vect)


class Intersection:

    def __init__(self, position, normal, object):
        self.position = position
        self.normal = normal
        self.object = object


def intersect(object, ray):
    """Return the intersection between object and ray"""
    if type(object) is Sphere:
        l = ray.direction / la.norm(ray.direction)
        o = ray.starting_point
        c = object.center
        r = object.rayon
        delta = (l.dot(o - c))**(2) - (la.norm(o - c))**(2) + r**(2)
        if delta < 0:
            return None  # No intersection between the ray and the object
        else:
            d1 = -(l.dot(o - c)) - np.sqrt(delta)
            d2 = -(l.dot(o - c)) + np.sqrt(delta)
            # Algebraic distance to the starting point of the intersection(s)
            if d1 <= 1e-6 and d2 <= 1e-6:
                return None  # No intersection ahead of the starting point
            else:
                if d1 * d2 >= 0:  # Two intersections ahead
                    d = min(d1, d2)
                    position = o + d * l
                    normal = (position - c) / la.norm(position - c)
                elif d1 * d2 < 0:  # Starting point in the sphere
                    d = max(d1, d2)
                    position = o + d * l
                    normal = - (position - c) / la.norm(position - c)
                intersection = Intersection(position, normal, object)
                return intersection

    if type(object) is Triangle:
        d = ray.direction / la.norm(ray.direction)
        o = ray.starting_point
        e1 = object.v1 - object.v0
        e2 = object.v2 - object.v0
        # Moller-Trumbore intersection algorithm
        p = np.cross(d, e2)
        det = e1.dot(p)
        if abs(det) < 1e-6:
            return None
        inv_det = 1. / det
        T = o - object.v0
        u = T.dot(p) * inv_det
        if u < 0 or u > 1:
            return None
        q = np.cross(T, e1)
        v = d.dot(q) * inv_det
        if v < 0 or u + v > 1:
            return None
        t = e2.dot(q) * inv_det
        if t > 1e-6:
            position = o + t * d
            normal = normalize(np.cross(e1, e2))
            if d.dot(normal) > 0:
                normal = - normal
            intersection = Intersection(position, normal, object)
            return intersection
