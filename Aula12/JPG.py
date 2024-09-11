import cv2
import numpy as np
import os

img =  cv2.imread("sample_.bmp")
img = cv2.resize(img,(512 ,  512))
print("Kb of img BMP = ",int(os.path.getsize("sample_.bmp")/1024))

cv2.imwrite("Sample8_JPG.jpg",img,(int(cv2.IMWRITE_JPEG_QUALITY),25))
img2 = cv2.imread("Sample8_JPG.jpg")
print("Kb of img2 JPG = ",int(os.path.getsize("Sample8_JPG.jpg")/1024))

cv2.imwrite("Sample7_JPG.jpg",img,(int(cv2.IMWRITE_JPEG_QUALITY),50))
img3 = cv2.imread("Sample7_JPG.jpg")
print("Kb of img2 JPG = ",int(os.path.getsize("Sample7_JPG.jpg")/1024))



imgs_concat =  np.concatenate((img,img2),axis=1)
imgs2 = np.concatenate((imgs_concat,img3),axis=1)

cv2.imshow("BMP X JPG ", imgs2)
cv2.waitKey(0)
