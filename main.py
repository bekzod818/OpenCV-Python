import cv2
import numpy as np

# photo

img = cv2.imread('images/blacktea.jpg')
img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
img = cv2.GaussianBlur(img, (3, 3), 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img = cv2.Canny(img, 200, 200)

kernel = np.ones((5, 5), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)

img = cv2.erode(img, kernel, iterations=1)

cv2.imshow('Result Image', img) # rasmni qirqish uchun img[50:150, 0:150]

cv2.waitKey(0) # vaqt beriladi millisekunda (1000 ms = 1 s, 0 bo'lsa cheksiz)
print(img.shape)

# video

# cap = cv2.VideoCapture('video/goal.mp4') # videoni ochish

# Web Kamerani ishga tushirish
# cap = cv2.VideoCapture(0)
# # o'lchamlarni sozlash
# cap.set(3, 500)
# cap.set(4, 400)
#
# while True:
#     success, img = cap.read()
#     cv2.imshow('Result Video', img)
#
#     # q bosilganda siklni to'xtaydi
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break
