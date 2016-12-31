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
            return None #No intersection between the ray and the object
        else:
            d1 = -(l.dot(o - c)) - np.sqrt(delta)
            d2 = -(l.dot(o - c)) + np.sqrt(delta)
            #Algebraic distance to the starting point of the intersection(s)
            t = [d1, d2]
            t = [t[i] for i in range(2) if t[i] >= 0]
            #Keep only the intersection ahead of the starting point of the ray
            if len(t) ==  0:
                return None #No intersection ahed of the starting point
            else:
                d = min(t)  #First intersection from the starting point
                position = o + d * l
                normal = (position - c) / la.norm(position - c)
                intersection = Intersection(position, normal, object)
                return intersection
