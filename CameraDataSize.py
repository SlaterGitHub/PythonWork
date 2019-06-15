import cv2
import CameraCompression as CC
import ImageDecompress as ID

cam = cv2.VideoCapture(0)

ret, image = cam.read()

cam.release()

file, rows = CC.compress(image)

cv2.imshow("frame", image)
cv2.waitKey(0)

image = ID.decompress(file, rows)
print(image.shape)

cv2.imshow("frame", image)
cv2.waitKey(0)
