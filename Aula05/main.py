#1)
'''''
import cv2
import numpy as np
img = cv2.imread('Image/taj_noise.jpg')
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
'''''
#2)

import cv2
import numpy as np
img = cv2.imread("Image/bola_pink_blue.jpg")
canny = cv2.Canny(img, 10,400)

cv2.imshow("entrada", img)
cv2.imshow("Saida Canny Altas ",canny)
cv2.waitKey(0)

#3)
'''''''''
import cv2 
import numpy as np
img = cv2.imread('Image/brain_noisy.png')
kernel = np.array([
    [1/5, 1/5, 1/5, 1/5, 1/5],
    [1/5, 1/5, 1/5, 1/5, 1/5],
    [1/5, 1/5, 1/5, 1/5, 1/5],
    [1/5, 1/5, 1/5, 1/5, 1/5],
    [1/5, 1/5, 1/5, 1/5, 1/5]
    ])

out = cv2.filter2D(img, -1, kernel)
cv2.imshow("entrada", img)
cv2.imshow("Saida Canny Altas ",out)
cv2.waitKey(0)
'''''''''
#4)
import cv2
import numpy as np
# img = cv2.imread('Image/taj_noise.jpg')
# median = cv2.medianBlur(img, 5)
#
# kernel = np.array([
#     [1/25, 1/25, 1/25, 1/25, 1/25],
#     [1/25, 1/25, 1/25, 1/25, 1/25],
#     [1/25, 1/25, 1/25, 1/25, 1/25],
#     [1/25, 1/25, 1/25, 1/25, 1/25],
#     [1/25, 1/25, 1/25, 1/25, 1/25]
#     ])
# media = cv2.filter2D(img,-1,kernel)
#
# cv2.imshow("entrada", img)
# cv2.imshow("media ",media)
# cv2.imshow("Final ",median)
# cv2.waitKey(0)