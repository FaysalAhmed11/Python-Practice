#haarcascade_frontalface_default.xml

import cv2

cascade_read = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
camera  = cv2.VideoCapture(0)

while True:
    c_rectangle, raw_image = camera.read()
    if not c_rectangle:
        break
    gray_image = cv2.cvtColor(raw_image, cv2.COLOR_BGR2GRAY)
    face = cascade_read.detectMultiScale(gray_image, 1.3,6)

    for(x,y,w,h) in face:
        cv2.circle(raw_image, (x,y), 40 , (0,0,200), 5)

    cv2.imshow('img', raw_image)
    key = cv2.waitKey(50) & 0xff

    if key == 50:
        break
camera.release()
cv2.destroyAllWindows()


