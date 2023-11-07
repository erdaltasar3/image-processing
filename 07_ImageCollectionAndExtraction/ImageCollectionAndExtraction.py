import cv2

img1 = cv2.imread("C:/Users/erdal/OneDrive/Belgeler/image-processing/images/d.jpg")
img2 = cv2.imread("C:/Users/erdal/OneDrive/Belgeler/image-processing/images/desen.png")



img1_weight = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
img2_weight = cv2.addWeighted(img1, 0.3, img2, 0.7, 0)

cv2.imshow("img1 weight", img1_weight)
cv2.imshow("img2 weight", img2_weight)

cv2.waitKey(0)
cv2.destroyAllWindows()