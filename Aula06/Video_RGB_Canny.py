import cv2
import numpy as np
cap = cv2.VideoCapture("videoSmall_flv.flv")
while (cap.isOpened()):
    ret, frame = cap.read()
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    can = cv2.Canny(frame, 10, 150)
    gray = cv2.cvtColor(can, cv2.COLOR_BGR2RGB)
    gray3c = cv2.cvtColor(gray, cv2.COLOR_BGR2RGB)
    fg = np.concatenate((frame,gray3c))
    imgplus = np.concatenate((frame, gray), axis=1)
    cv2.imshow("Original X Cinza ", imgplus)
    if (cv2.waitKey(int(1000 / 30)) & 0xFF == ord('q')):
        break
#cv2.waitKey(0)
