import cv2

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('naruto.png')

cv2.imshow('face detector', img)

cv2.waitKey()