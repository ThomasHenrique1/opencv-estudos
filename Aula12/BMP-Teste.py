import cv2
import numpy as np
import os

img =  cv2.imread("sample_.bmp")
img = cv2.resize(img,(512 ,  512))
print("Kb pf img BMP = ",int(os.path.getsize("sample_.bmp")/1024))

cv2.imwrite("Sample2_JPG.jpg",img,(int(cv2.IMWRITE_JPEG_QUALITY),100))

img2 = cv2.imread("Sample2_JPG.jpg")
print("Kb of img2 JPG = ",int(os.path.getsize("Sample2_JPG.jpg")/1024))

imgs_concat =  np.concatenate((img,img2),axis=1)

cv2.imshow("BMP X JPG ", imgs_concat)
cv2.waitKey(0)
