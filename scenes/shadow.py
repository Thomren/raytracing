# -*- coding: utf-8 -*-


class Sphere:

    def __init__(self, center, rayon, material):
        self.center = center
        self.rayon = rayon
        self.material = material


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
