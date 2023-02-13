import copy
import cv2
from skimage.draw import polygon
import numpy as np

x1 = 350
y1 = 131
x2 = 98
y2 = 50
w = 50

tan = (y1 - y2) / (x2 - x1)
angle = np.arctan(tan)

points = []
points.append([y1 - w / 2 * np.cos(angle), x1 - w / 2 * np.sin(angle)])
points.append([y2 - w / 2 * np.cos(angle), x2 - w / 2 * np.sin(angle)])
points.append([y2 + w / 2 * np.cos(angle), x2 + w / 2 * np.sin(angle)])
points.append([y1 + w / 2 * np.cos(angle), x1 + w / 2 * np.sin(angle)])
points = np.array(points)
rr, cc = polygon(points[:, 0], points[:, 1], (480, 640))	# 得到举行中所有点的行和列
# print(rr, cc)

# 可视化对比
im = cv2.imread('10/pcd1000r.png')
im2 = copy.deepcopy(im)
cv2.line(im, (x1, y1), (x2, y2), (255, 0, 0), w)
for i in range(rr.shape[0]):
    cv2.circle(im2, (cc[i], rr[i]), 1, (0, 255, 0), -1)

cv2.imshow('im', im)
cv2.imshow('im2', im2)

cv2.waitKey()

