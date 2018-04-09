import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage

# fetch image
imageRead = ndimage.imread('rotated.png')

# function for angle between two vectors
def angleFromVecs(v1, v2):
    vectorCos = np.dot(v1,v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))
    # print (vectorCos)
    rad = np.arccos(np.clip(vectorCos, -1.0, 1.0))
    # print np.rad2deg(rad)
    return np.rad2deg(rad)