import cv2
import numpy
import lz4.frame
from time import sleep

x = 640
y = 480

vid = cv2.VideoCapture(0)

sleep(0.1)

while True:
    try:
        ret, image = vid.read()
        size1 = image.size()
        print(size1)
        image = lz4.frame.compress(image)
        size2 = image.size()
        print(size2)
        image = (numpy.fromstring(lz4.frame.decompress(image), dtype = "uint8")).reshape((y, x, 3))
        cv2.imshow("hi", image)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
    except:
        print("error")
vid.release()
