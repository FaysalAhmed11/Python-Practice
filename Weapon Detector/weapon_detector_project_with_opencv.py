import numpy as np
import cv2
import imutils

# Load the trained classifier for gun detection
gun_cascade = cv2.CascadeClassifier('cascade.xml')

# Open the webcam
camera = cv2.VideoCapture(0)

firstFrame = None

while True:
    ret, frame = camera.read()
    if not ret:
        break  # Exit the loop if the camera is not capturing properly

    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Fix function name (was detecMultiScale, should be detectMultiScale)
    gun = gun_cascade.detectMultiScale(gray, 1.3, 5, minSize=(100, 100))

    # Reset gun_exist flag
    gun_exist = False  

    # Draw rectangles around detected guns
    for (x, y, w, h) in gun:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        gun_exist = True  # If a gun is detected, set the flag to True

    # Fix firstFrame typo
    if firstFrame is None:
        firstFrame = gray
        continue

    cv2.imshow("Security Feed", frame)
    
    # Exit if 'q' is pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

    # Print correct detection status
    if gun_exist:
        print("GUN DETECTED!")
    else:
        print("NO GUN DETECTED")

# Release camera and close windows properly
camera.release()
cv2.destroyAllWindows()
