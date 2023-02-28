import cv2
import numpy as np

img = np.zeros((512,512,3))

"""
cv2.line(img,(0,0),(511,511),(255,0,0),10)
cv2.line(img,(0,511),(511,0),(0,255,255),10)

"""

cv2.rectangle(img,(50,100),(450,300),(255,0,0),3)
font = cv2.FONT_ITALIC
cv2.putText(img,"Opencv",(150,220),font,2,(0,0,255),3,cv2.LINE_AA)

cv2.imshow("resim",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


"""
cv2.line
1. parametre = hangi resime uygulanacagi
2.parametre = 1. x ve y kordinatlari
3. parametre = 2. x ve y kordinatlari
4. parametre = renk secimi
5. parametre = cizgi kalinligi
"""

"""
cv2.rectangle, cv2.circle, cv2.ellipse gibi metotlarda 
cv2.line gibi benzer ozellikleri kullanir

"""



"""
cv2.putText

1. parametre = hangi resime uygulanacagi
2. parametre = hangi yazinin yazilacagi
3. parametre = sol alt kose kordinatlari
4. parametre = yazi tipi
5. parametre = yazi buyuklugu
6. parametre = renk
7. parametre = cizgi kalinligi
8. parametre = line type
"""