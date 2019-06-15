import cv2
import numpy
from time import sleep, time
import ColorSplitter as CS
import GraphPlot as gp

def compress(image):
    Splitter = CS.ColorSplitter()
    image = Splitter.removeZeros(image)
    colors = Splitter.addColors(image)
    colors = Splitter.removeRepetitions(colors)
    colors, rowLengths = Splitter.flattenImage(colors)
    colors = Splitter.addIndexes(colors, False)
    colors = Splitter.sortColors(colors)
    colors = Splitter.proportionColors(colors)

    graph = gp.Graph()
    colorGraphs = [[],[],[]]
    colorGraphs[0] = graph.getLineEquation(colors, 0, 3)
    colorGraphs[1] = graph.getLineEquation(colors, 1, 3)
    colorGraphs[2] = graph.getLineEquation(colors, 2, 3)

    exportImage = []
    exportImage.append(colorGraphs)
    exportImage.append([i[3:6] for i in colors])

    return exportImage, rowLengths
