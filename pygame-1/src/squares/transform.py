import numpy as np
import math as m

def create_translation_matrix(dx, dy):
    return np.array([[1, 0, dx],
                     [0, 1, dy],
                     [0, 0, 1]])

def create_scaling_matrix(sx, sy):
    return np.array([[sx, 0, 0],
                     [0, sy, 0],
                     [0, 0, 1]])

def create_rotation_matrix(angle):
    cos_a = m.cos(angle)
    sin_a = m.sin(angle)
    return np.array([[cos_a, sin_a, 0],
                     [-sin_a, cos_a, 0],
                     [0, 0, 1]])