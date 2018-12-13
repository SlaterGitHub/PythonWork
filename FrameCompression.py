import cv2
import numpy
import lz4.frame
from time import sleep

x = 640
y = 480

vid = cv2.VideoCapture(0)

sleep(1)

while True:
    ret, image = vid.read()
    image = lz4.frame.compress(image)
    image = (numpy.fromstring(lz4.frame.decompress(image), dtype = "uint8")).reshape((y, x, 3))
    cv2.imshow("hi", image)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
