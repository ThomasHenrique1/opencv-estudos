import cv2

img = cv2.imread("Image/face_a.jpg")
crop = img[162:187 , 68:137]
cv2.imshow("Original", img)
cv2.imshow("Crop", crop)

cv2.waitKey(0)