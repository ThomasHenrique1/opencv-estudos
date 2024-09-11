# Import all essential libraries
import cv2
import numpy as np

# minRange for min skin color Range
# maxRange for maximum skin color Range
minRange = np.array([0,133,77],np.uint8)
maxRange = np.array([235,173,127],np.uint8)
image = cv2.imread("lena_color_128_128_.jpg")

# change our image bgr to ycr using cvtcolor() method
YCRimage = cv2.cvtColor(image,cv2.COLOR_BGR2YCR_CB)

# apply min or max range on skin area in our image
skinArea = cv2.inRange(YCRimage,minRange,maxRange)
detectedSkin = cv2.bitwise_and(image, image, mask = skinArea)

#show results
cv2.imshow("1_HSV.jpg",skinArea )
cv2.imshow("2_YCR.jpg",YCRimage)
cv2.imshow("3_global_result.jpg",detectedSkin)
cv2.imshow("Image.jpg",image)

cv2.waitKey(0)
cv2.destroyAllWindows()