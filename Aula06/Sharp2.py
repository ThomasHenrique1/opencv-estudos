#Sharpening
import cv2
import numpy as np
cap = cv2.VideoCapture("videoSmall_flv.flv")
while (cap.isOpened()):
    ret, frame = cap.read()
    can = cv2.Canny(frame, 10, 150)
    kernel = np.array([[-1, -1, -1],
                       [-1, 9, -1],
                       [-1, -1, -1]])

    sharp = cv2.filter2D(frame, -1, kernel)
    imgplus = np.concatenate((frame, sharp), axis=1)
    cv2.imshow("Original X Cinza ", imgplus)
    if (cv2.waitKey(int(1000 / 30)) & 0xFF == ord('q')):
        break
#cv2.waitKey(0)
