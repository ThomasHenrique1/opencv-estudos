#Sharpening
import cv2
import numpy as np
cap = cv2.VideoCapture("videoSmall_flv.flv")
while (cap.isOpened()):
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([100,127,127])
    upper_blue = np.array([160, 127, 127])

    mask = cv2.inRange(hsv,lower_blue,upper_blue)
    res = cv2.bitwise_and(frame,frame,mask=mask)
    imgplus = np.concatenate((frame, res), axis=1)
    cv2.imshow("Original X Cinza ", imgplus)
    if (cv2.waitKey(int(1000 / 30)) & 0xFF == ord('q')):
        break
#cv2.waitKey(0)