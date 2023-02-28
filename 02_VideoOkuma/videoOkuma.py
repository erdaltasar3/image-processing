import cv2

# % part1
""" 

cam = cv2.VideoCapture(0)

while True:

    ret, frame = cam.read()

    if ret == False:
        print("Kameradan goruntu alinamadi")
        break

   # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # gelen gpruntuyu siyah-beyaz yapar
    cv2.imshow("frame",frame)

    if cv2.waitKey(1) & 0xFF == ord("q"): # waitkey'in icine yazilan sayiyi artirirsak agir cekim olusur
        print("Goruntu sonlandirildi")
        break

cam.release()
cv2.destroyAllWindows()
"""

# % part2

cam = cv2.VideoCapture("walkingPeoples.mp4")

while True:

    ret, frame = cam.read()

    if not ret:
        print("goruntu alinamadi")
        break
    
    cv2.imshow("kamera",frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("kamera kapatildi")
        break

cam.release()
cv2.destroyAllWindows()