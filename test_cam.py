import cv2

cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    if not success:
        break
    cv2.imshow('Test Webcam', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()
print('Webcam test complete. Press ESC to exit.')

