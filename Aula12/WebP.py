import cv2
import numpy as np
import os

img =  cv2.imread("sample_.bmp")
img = cv2.resize(img,(512 ,  512))
print("Kb of img BMP = ",int(os.path.getsize("sample_.bmp")/1024))


cv2.imwrite("Sample5_WebP.webp",img,(int(cv2.IMWRITE_WEBP_QUALITY),25))
img3= cv2.imread("Sample5_WebP.webp")
print("Kb of img3 WebP = ",int(os.path.getsize("Sample5_WebP.webp")/1024))

cv2.imwrite("Sample4_WebP.webp",img,(int(cv2.IMWRITE_WEBP_QUALITY),50))
img2 = cv2.imread("Sample4_WebP.webp")
print("Kb of img2 WebP = ",int(os.path.getsize("Sample4_WebP.webp")/1024))

imgs_concat =  np.concatenate((img,img2),axis=1)
imgs2 =  np.concatenate((imgs_concat,img3),axis=1)

cv2.imshow("BMP X WebP ", imgs2)
cv2.waitKey(0)
