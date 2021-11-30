import cv2
import numpy as np

photo = np.zeros((450, 450, 3), dtype="uint8")

# RGB - standart
# BGR - format OpenCV
# photo[10:200, 50:250] = 119, 201, 105

 # to'rtburchak chizish
cv2.rectangle(photo, (50, 50), (120, 120), (119, 201, 105), thickness=cv2.FILLED)

# chiziq chizish
cv2.line(photo, (0, photo.shape[0] // 2), (photo.shape[1], photo.shape[0] // 2), (119, 201, 105), thickness=3)

# aylana doira chizish
cv2.circle(photo, (photo.shape[1] // 2, photo.shape[0] // 2), 50, (119, 201, 105), thickness=cv2.FILLED)
cv2.circle(photo, (photo.shape[1] // 2, photo.shape[0] // 2), 90, (0, 0, 255), thickness=3)

# text yozish
cv2.putText(photo, "OpenCV", (200, 80), cv2.FONT_HERSHEY_TRIPLEX, 1.2, (255, 0, 0), 4)

cv2.imshow("Photo", photo)
cv2.waitKey(0)
