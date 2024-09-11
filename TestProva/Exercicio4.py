
import cv2
import numpy as np
image = cv2.imread('Image/Draco.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh, bw = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
Canny3c = cv2.cvtColor(bw, cv2.COLOR_BGR2RGB)

compare = np.concatenate((image, Canny3c), axis=1)
cv2.imshow('preto e branco', compare)
cv2.waitKey(0)


