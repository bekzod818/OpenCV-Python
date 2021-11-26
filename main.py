import cv2

# photo

# img = cv2.imread('images/blacktea.jpg')
# cv2.imshow('Result Image', img)
#
# cv2.waitKey(0) # vaqt beriladi millisekunda (1000 ms = 1 s, 0 bo'lsa cheksiz)

# video

# cap = cv2.VideoCapture('video/goal.mp4') # videoni ochish

# Web Kamerani ishga tushirish
cap = cv2.VideoCapture(0)
# o'lchamlarni sozlash
cap.set(3, 500)
cap.set(4, 400)

while True:
    success, img = cap.read()
    cv2.imshow('Result Video', img)

    # q bosilganda siklni to'xtaydi
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
