import cv2

video = cv2.VideoCapture(0)

video.set(3,20)
video.set(4,10)

while True:

    ret, frame = video.read()

    cv2.imshow("frame", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
