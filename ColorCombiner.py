import cv2
import numpy

class decompress:
    def addRepetitions(self, imageArray):
        image = []
        for x in range(len(imageArray)):
            for z in range(imageArray[x][3]):
                image.append(imageArray[x][:3])
        return image
    def make2D(self, imageArray, rowLengths):
        image = []
        for x in range(len(rowLengths)):
            image.append(imageArray[:rowLengths[x]])
        return image

    def orderImage(self, imageArray):
        return sorted(imageArray, key=lambda y: y[4])

    def applyEqu(self, file):
        rgbArray = []
        imageArray = []
        for x in range(len(file[1])):
            for y in range(3):
                color = round((file[0][y][0]*file[1][x][0]) + file[0][y][1])
                if color < 0:
                    color = 0
                rgbArray.append(int(color))
            rgbArray.append(file[1][x][1])
            rgbArray.append(file[1][x][2])
            imageArray.append(rgbArray)
            rgbArray = []

        return imageArray
