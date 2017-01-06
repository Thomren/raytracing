# -*- coding: utf-8 -*-
import numpy as np
from numpy import linalg as la
from scene import *


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
