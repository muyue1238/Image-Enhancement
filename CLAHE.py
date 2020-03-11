import numpy as np
import cv2

img = cv2.imread('cat.png')

# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
# cl1 = clahe.apply(img)
(b, g, r) = cv2.split(img)
bH = clahe.apply(b)
gH = clahe.apply(g)
rH = clahe.apply(r)

result = cv2.merge((bH, gH, rH))

cv2.imwrite('clahe_dst.jpg',result)
