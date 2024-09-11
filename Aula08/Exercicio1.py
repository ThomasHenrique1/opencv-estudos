import cv2
import numpy as np
img = cv2.imread('Image/riuori.jpg')
kernel_Prewitt_y = np.array([  # matriz y - Vertical
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]])
kernel_Prewitt_x = np.array([  # matriz y - Horizontal
    [1, 1, 1],
    [0, 0, 0],
    [-1, -1, -1]])
destX = cv2.filter2D(img,-1,kernel_Prewitt_x )
destY = cv2.filter2D(img,-1,kernel_Prewitt_y )
cv2.imshow("entrada", img)
cv2.imshow("Saida alta X-H ",destX)
cv2.imshow("Saida alta Y-H ",destY)
cv2.waitKey(0)
