import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage

# fetch image
imageRead = ndimage.imread('rotated.tiff')

# function for angle between two vectors
def angleFromVecs(v1, v2):
    vectorCos = np.dot(v1,v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))
    # print (vectorCos)
    rad = np.arccos(np.clip(vectorCos, -1.0, 1.0))
    print np.rad2deg(rad)
    return np.rad2deg(rad)

# find the two corners
nz = imageRead.nonzero()
leftix = np.argmin(nz[0])
# print leftix
rightix = np.argmax(nz[1])
# print rightix

cord1 = np.array([nz[1][leftix],nz[0][leftix]])
# print cord1
cord2 = np.array([nz[1][rightix],nz[0][rightix]])
# print cord2
