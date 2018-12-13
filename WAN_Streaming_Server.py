import socket
import cv2
import numpy
from time import sleep

x = 320
y = 240
i = True

host = '192.168.0.14'
host = '172.23.5.114'
port = 5000
#host = 'localhost'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def connect(i):
    print(port)
    while i == True:
        try:
            s.connect((host, port))
            print("connected")
            return False
        except:
            sleep(1)
def getText(i):
    global port
    while i == False:
        try:
            text = s.recv(10)
            text = int(text)
            if text != None:
                print(text)
        except:
            s.close()
            port += 50
            return True
            
while True:
    if i == True:
        i = connect(i)
    elif i == False:
        i = getText(i)
        

"""def recvImg(s):
    frame = recvall(s)
    if not frame:
        return None
    frame = numpy.fromstring(frame, dtype = numpy.uint8)
    return frame.reshape((y, x, 3))

def recvall(s):
    No.Datas = 230400
    totalData = b''
    while len(totalData) < No.Datas:
        data = s.recv(No.Datas - len(totalData))
        if not data:
            return None
        totalData += data
    return totalData

while True:
    frame = recv_msg(s)
    frame = cv2.resize(frame, (1280, 960), interpolation = cv2.INTER_AREA)
    cv2.imshow("HomeCam", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        s.send('q')
        break
time.sleep(0.5)
cv2.destroyAllWindows()
s.close()"""
