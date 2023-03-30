import cv2
from tkinter import colorchooser

color_to_find = (0, 0, 0)

def choose_color():
    global color_to_find
    color_code = colorchooser.askcolor(title = "Choose color")
    color_to_find = color_code[0]

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 60)

while True:
    ret, frame = cap.read()

    mask = cv2.inRange(frame, color_to_find, color_to_find)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('result', frame)

    pressedKey = cv2.waitKey(1) & 0xFF
    if pressedKey == ord('c'):
        choose_color()
        print(color_to_find)
    elif pressedKey == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()