import cv2
import numpy as np


def nothing(x):
    pass

img = np.zeros((512,512,3),np.uint8)

cv2.namedWindow("resim")

cv2.createTrackbar("R","resim",0,255,nothing)
cv2.createTrackbar("G","resim",0,255,nothing)
cv2.createTrackbar("B","resim",0,255,nothing)

while (1):
    cv2.imshow("resifm",img)

    if (cv2.waitKey(1) & 0xFF == ord("q")):
        break

    r = cv2.getTrackbarPos("R","resim")
    g = cv2.getTrackbarPos("G","resim")
    b = cv2.getTrackbarPos("B","resim")

    img[:] = [b,g,r]

cv2.destroyAllWindows()