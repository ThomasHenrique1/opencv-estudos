import cv2
import numpy as np
img = cv2.imread('taj_noise.jpg')
kernel_Prewitt_y = np.array([  # matriz y - Vertical
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]])
kernel_Prewitt_x = np.array([  # matriz x - Horizontal
    [1, 1, 1],
    [0, 0, 0],
    [-1, -1, -1]])
destY = cv2.filter2D(img, -1, kernel_Prewitt_y)
destX = cv2.filter2D(img, -1, kernel_Prewitt_x)
cv2.imshow("Orignal", img)
cv2.imshow("Dest Y-V", destY)
cv2.imshow("Dest X-H", destX)
cv2.waitKey(0)
