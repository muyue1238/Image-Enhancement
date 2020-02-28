import cv2

img = cv2.imread("cat.png", 1)

(b, g, r) = cv2.split(img)
bH = cv2.equalizeHist(b)
gH = cv2.equalizeHist(g)
rH = cv2.equalizeHist(r)

result = cv2.merge((bH, gH, rH))
cv2.imwrite("rgb_dst.png", result)
