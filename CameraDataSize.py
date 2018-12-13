import cv2
import lz4.frame
from time import sleep

video = cv2.VideoCapture(0)

video.set(3,320)
video.set(4,240)

sleep(1)

while True:
    ret, frame = video.read()
    size1 = frame.size()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    size2 = frame.size()
    image = lz4.frame.compress(frame)
    size3 = len(image)
    cv2.imshow("output", frame)

    print(size1)
    print(size2)
    print(size3)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break
