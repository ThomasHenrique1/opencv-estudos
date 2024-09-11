import cv2
import numpy as np
import os

img =  cv2.imread("sample_.bmp")
img = cv2.resize(img,(512 ,  512))
print("Kb of img BMP = ",int(os.path.getsize("sample_.bmp")/1024))

cv2.imwrite("Sample3_PNG.png",img,(int(cv2.IMWRITE_PNG_COMPRESSION),25))
img2 = cv2.imread("Sample3_PNG.png")
print("Kb of img2 PNG = ",int(os.path.getsize("Sample3_PNG.png")/1024))

cv2.imwrite("Sample6_PNG.png",img,(int(cv2.IMWRITE_PNG_COMPRESSION),50))
img3 = cv2.imread("Sample6_PNG.png")
print("Kb of img6 PNG = ",int(os.path.getsize("Sample6_PNG.png")/1024))


imgs_concat =  np.concatenate((img,img2),axis=1)
imgs2 = np.concatenate((imgs_concat,img3),axis=1)

cv2.imshow("BMP X PNG ", imgs2)
cv2.waitKey(0)
