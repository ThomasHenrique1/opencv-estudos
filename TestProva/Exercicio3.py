import cv2


img = cv2.imread("Image/face_a.jpg")
img2 = cv2.imread("Image/hand_b.jpg")
# crop =  img[y:y+a , x:x+b]

crop = img[96:137:, 49:155]  # Arruma os numeros para o OPENCV fazer o corte na imagem
cv2.imshow("Original", img)
cv2.imshow("Crop", crop)

crop2 = img2[155:201:, 179:270]
cv2.imshow("Original", img2)
cv2.imshow("Crop2", crop2)

cv2.waitKey(0)
