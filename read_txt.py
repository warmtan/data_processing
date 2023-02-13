import numpy as np 
import cv2
from skimage.draw import polygon

im = cv2.imread('10/pcd1000r.png')
source = np.loadtxt('10/pcd1000cpos.txt')
print(source[0][0])


