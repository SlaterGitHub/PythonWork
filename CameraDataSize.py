import cv2
import lz4.frame
import lz4.block
from time import sleep

video = cv2.VideoCapture(0)

sleep(1)

def compressUntil(size, image):
    if (len(image) <= size):
        return image
    image = lz4.block.compress(image)
    print(len(image))
    compressUntil(size, image)

while True:
    ret, frame = video.read()
    size1 = frame.size
    image = lz4.frame.compress(frame)
    size3 = len(image)
    image = compressUntil(430000, image)
    size4 = len(image)
    cv2.imshow("output", frame)
    print(size1)
    print(size3)
    print(size4)
    #sleep(1)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break
