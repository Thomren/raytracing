# -*- coding: utf-8 -*-
from ray import *
import numpy as np

class Camera :
    def __init__(self, image_nrows, image_ncols, focal_length) :
        self.image_nrows = image_nrows
        self.image_ncols = image_ncols
        self.focal_length = focal_length
        
    def ray_at(self, row, col) :
        direction = np.array([1-row/(self.image_nrows/2), 
                              1-(col/(self.image_ncols/2)), 
                                self.focal_length])
        starting_point = np.array([0, 0, 0])
        ray = Ray(direction, starting_point)
        return ray
