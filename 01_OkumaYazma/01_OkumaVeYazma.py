import cv2

resim = cv2.imread("Images/kizkulesi.jpg",0) # ,0 ifadesi girilen resmi siyah beyaz yapar.

cv2.imshow("resim penceresi",resim)
k = cv2.waitKey(0)

if k == ord("q"):
    print("gri resim kaydedildi ! ")
    cv2.imwrite("kizKulesiGri.jpg",resim)
if k == ord(" "):
    print("cikis yapildi !")



cv2.destroyAllWindows()