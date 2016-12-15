# -*- coding: utf-8 -*-
import numpy as np
from numpy import linalg as la

class Spotlight :
    def __init__(self, position, color) :
        self.position = position
        self.color = color
        
def phong_illuminate (scene, intersection, viewer) :
    m = intersection.object.material
    nblights = len(scene.lights)
    ks, kd, ka, alpha = m.specular, m.diffuse, m.ambiant, m.shininess
    n = intersection.normal / la.norm(intersection.normal)
    l = [scene.lights[i].position - intersection.position for i in range(nblights)]
    r = [2*(l[i].dot(n))*n-l[i] for i in range(nblights)]
    v = viewer - intersection.position
    ip = ka
    for k in range (nblights) :
        ip += kd*(l[k].dot(n))+ks*(r[k].dot(v))**(alpha)
    res = np.array([0.,0.,0.])
    for k in range (nblights) :
        res += m.color.dot(scene.lights[k].color)
    return ip*res
    