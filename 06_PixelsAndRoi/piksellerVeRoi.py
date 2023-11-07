import cv2
import matplotlib.pyplot as plt


img = cv2.imread("C:/Users/erdal/OneDrive/Belgeler/image-processing/images/ucak.jpg")

cv2.namedWindow("img", cv2.WINDOW_NORMAL)

# print(img.shape) resim boyutu ogrenme

roi = img[0:400,400:1000] # kesilen parca boyutlari

img[100:500,600:1200] = roi # önce y sonra x


cv2.imshow("img", img)


cv2.waitKey()
cv2.destroyAllWindows()


"""


np.max(img)


img = cv2.imread("images/cv2.png")

B = img[:,:,0]
G = img[:,:,1]
R = img[:,:,2]


cv2.imshow("original",img)
cv2.imshow("B",B)
cv2.imshow("g",G)
cv2.imshow("R",R)

cv2.waitKey()
cv2.destroyAllWindows()


"""