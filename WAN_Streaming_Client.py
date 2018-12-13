import socket
import time
import cv2
import numpy

video = cv2.VideoCapture(0)

time.sleep(0.1)

host = "localhost"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((, 5002))

s.listen(10)
c, addr = s.accept()

print("{} connected".format(addr))

while True:
    ret, frame = video.read()

    frame = frame.flatten()
    datas = frame.tostring()

    c.sendall(datas)

    key = cv2.waitKey(1) & 0xFF

    if s.recv == 'q':
        break

video.release()
cv2.destoryAllWindows()
s.close()
