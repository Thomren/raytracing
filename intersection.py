# -*- coding: utf-8 -*-
import numpy as np
from numpy import linalg as la
from scene import *

class Intersection :
    def __init__(self, position, normal, object) :
        self.position = position
        self.normal = normal
        self.object = object

def minpositive(t) :
    """Return the smallest positive element of t, -1 if it isn't exist"""
    pos = [t[i] for i in range(len(t)) if t[i]>=0]
    if pos == [] :
        return -1
    else :
        return min(pos)
        
def intersect(object, ray) :
    if type(object) is Sphere :
        l = ray.direction/la.norm(ray.direction)
        o = ray.starting_point
        c = object.center
        r = object.rayon
        delta = (l.dot(o-c))**(2)-(la.norm(o-c))**(2)+r**(2)
        if delta < 0 :
            return None
        else :
            d1 = -(l.dot(o-c))-np.sqrt(delta)
            d2 = -(l.dot(o-c))+np.sqrt(delta)
            d = minpositive([d1, d2])
            if d < 0 :
                return None
            else :
                position = o+d*l
                normal = (position - c) / la.norm(position - c)
                intersection = Intersection(position, normal, object)
                return intersection
                    
        
    

