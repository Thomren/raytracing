# Show to python where to find the Camera module
import sys
sys.path.append('..')

import numpy as np
from numpy import linalg as la
from camera import *

c = Camera(100, 200, 3)

r_center = c.ray_at(c.image_nrows / 2, c.image_ncols / 2);

assert abs(r_center.direction.dot(np.array([0,0,1])) - la.norm(r_center.direction)) < 0.01, "c.ray_at(c.image_nrows / 2, c.image_ncols / 2) should have the direction [0,0,1].";

r_zero = c.ray_at(0,0);

r_zero_ref_dir = np.array([1,1,c.focal_length])
r_zero_ref_dir = r_zero_ref_dir / la.norm(r_zero_ref_dir)

assert abs(r_zero.direction.dot(r_zero_ref_dir) -
           la.norm(r_zero.direction)) < 0.01, "c.ray_at(0,0) should have the direction [1,1,camera.focal_length].";

r_one = c.ray_at(c.image_nrows, c.image_ncols);
r_one_ref_dir = np.array([-1,-1,c.focal_length])
r_one_ref_dir = r_one_ref_dir / la.norm(r_one_ref_dir)

assert abs(r_one.direction.dot(r_one_ref_dir) -
           la.norm(r_one.direction)) < 0.01, "c.ray_at(c.nrows,c.ncols) should have the direction [-1,-1,c.focal_length].";
