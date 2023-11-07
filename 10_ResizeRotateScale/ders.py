import cv2

img = cv2.imread("C:/Users/erdal/OneDrive/Belgeler/image-processing/images/1.jpeg")


# resmi yeniden boyutlandirma
res = cv2.resize(img, (300,300))
# res1 = cv2.imshow(img, None, fx=0.5, fy=0.5, interpolation= cv2.INTER_CUBIC)

cv2.imshow("img", img)
cv2.imshow("res", res)




cv2.waitKey()
cv2.destroyAllWindows()