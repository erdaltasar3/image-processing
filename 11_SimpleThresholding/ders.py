import cv2
import matplotlib.pyplot as plt

resim = cv2.imread("C:/Users/erdal/OneDrive/Belgeler/image-processing/images/gradient.jpg")


_, thresh1 = cv2.threshold(resim,182, 255, cv2.THRESH_BINARY)
_, thresh2 = cv2.threshold(resim,182, 255, cv2.THRESH_BINARY_INV)
_, thresh3 = cv2.threshold(resim,182, 255, cv2.THRESH_TRUNC)
_, thresh4 = cv2.threshold(resim,182, 255, cv2.THRESH_TOZERO)
_, thresh5 = cv2.threshold(resim,182, 255, cv2.THRESH_TOZERO_INV)

resimler = [resim, thresh1, thresh2, thresh3, thresh4, thresh5]
basliklar = ["original","thresh1","thresh2","thresh3","thresh4","thresh5",]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(resimler[i],"gray"),plt.title(basliklar[i])
    
plt.show()

"""
myResult = cv2.inRange(img,100,130)
cv2.imshow("esikleme", myResult)
"""