import cv2

img1 = cv2.imread("C:/Users/erdal/OneDrive/Belgeler/image-processing/images/ucak.jpg")
img2 = cv2.imread("C:/Users/erdal/OneDrive/Belgeler/image-processing/images/desen.png")

cv2.namedWindow("img1", cv2.WINDOW_NORMAL)


# img2 gri tona cevir
img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# treshold islemi
ret, mask = cv2.threshold(img2_gray, 10, 255, cv2.THRESH_BINARY) # 10 pikselin uzerindekileri 255 yap

# mask inv
mask_inv = cv2.bitwise_not(mask)

# roi
x,y,_ = img2.shape

roi = img1[0:x,0:y]

#
img2_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

toplam = cv2.add(img2_bg, img2_fg)

img1[0:x,0:y] = toplam





cv2.imshow("img2", img2)
cv2.imshow("img2 gray", img2_gray)
cv2.imshow("mask", mask)
cv2.imshow("mask inv", mask_inv)
cv2.imshow("roi", roi)
cv2.imshow("img2 bg", img2_bg)
cv2.imshow("img2 fg", img2_fg)
cv2.imshow("toplam", toplam)
cv2.imshow("img1", img1)


cv2.waitKey()
cv2.destroyAllWindows()