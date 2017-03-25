# -*- coding: utf-8 -*-
import numpy as np


class Scene:

    def __init__(self):
        self.objects = []
        self.lights = []

    def add_object(self, o):
        self.objects.append(o)

    def add_light(self, l):
        self.lights.append(l)


class Material:

    def __init__(self, color, ambiant, diffuse,
                 specular, shininess, reflection):
        self.color = color
        self.ambiant = ambiant
        self.diffuse = diffuse
        self.specular = specular
        self.shininess = shininess
        self.reflection = reflection


class Sphere:

    def __init__(self, center, rayon, material):
        self.center = np.array(center)
        self.rayon = rayon
        self.material = material


class Triangle:

    def __init__(self, v0, v1, v2, material):
        self.v0 = np.array(v0)
        self.v1 = np.array(v1)
        self.v2 = np.array(v2)
        self.material = material


class Plane:

    def __init__(self, v0, v1, v2, v3, material):
        self.v0 = np.array(v0)
        self.v1 = np.array(v1)
        self.v2 = np.array(v2)
        self.v3 = np.array(v3)
        self.material = material
