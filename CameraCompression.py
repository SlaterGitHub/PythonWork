import cv2
import numpy
from time import sleep, time
import ColorSplitter as CS

redDone = None
greenDone = None
blueDone = None

red = None
blue = None
green = None

def prepCamera():
    cam = cv2.VideoCapture(0)
    return cam

def closeCamera(camera):
    camera.release()

def takePhoto(camera):
    ret, image = camera.read()
    return image

def main():
    camera = prepCamera()
    time1 = time()
    image = takePhoto(camera)
    Splitter = CS.ColorSplitter()
    image = Splitter.removeZeros(image)
    colors = Splitter.addColors(image)
    colors = Splitter.removeRepetitions(colors)
    colors = Splitter.addIndexes(colors)
    colors, rowLengths = Splitter.flattenImage(colors)
    colors = Splitter.sortColors(colors)
    time2 = time()
    print(time2-time1)

if '__main__':
    main()
