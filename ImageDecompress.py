import cv2
import numpy as np
import ColorCombiner as CC

def decompress(file, rows):
    comb = CC.decompress()
    imageArray = comb.applyEqu(file)
    imageArray = comb.orderImage(imageArray)
    #imageArray = comb.make2D(imageArray, rows)
    imageArray = comb.addRepetitions(imageArray)
    imageArray = np.array(imageArray, dtype = "uint8")
    image = imageArray.reshape((len(rows), int(len(imageArray)/len(rows)), 3))
    return image
