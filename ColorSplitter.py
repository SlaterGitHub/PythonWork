from threading import Thread
import MergeSort as ms
import numpy as np

class ColorSplitter:
    def flattenImage(self, colors):
        tempArray = []
        rowLengths = []
        x=0
        y=0
        while(x < len(colors)):
            while(y < len(colors[x])):
                tempArray.append(colors[x][y])
                y+=1
            rowLengths.append(y)
            y=0
            x+=1

        return tempArray, rowLengths

    def removeZeros(self, image):
        loop1, loop2, g = image.shape

        x = 0
        y = 0

        while(x < loop1):
            if (not np.any(image[x])):
                image = np.delete(image, [x], axis = 0)
                loop1 += -1
            else:
                x += 1

        return image

    def removeRepetitions(self, colors):
        y=0
        x=0
        z=1
        while(y < len(colors)-1):
            while(x < len(colors[y])-1):
                if (colors[y][x][0] == colors[y][x+1][0]) and (colors[y][x][1] == colors[y][x+1][1]) and (colors[y][x][2] == colors[y][x+1][2]):
                    colors[y].pop(x+1)
                    z+=1
                else:
                    colors[y][x].append(z)
                    z=1
                    x+=1
            y+=1
            x=0
        return colors

    def sortColors(self, colors):
        colors = sorted(colors, key=lambda y: y[3])

        return colors

    def addIndexes(self, colors):
        x=0
        y=0

        while(y < len(colors)):
            while(x < len(colors[y])):
                colors[y][x].append(y+x)
                x+=1
            y+=1
            x=0

        return colors

    def addColors(self, colors):
        loop1, loop2, d = colors.shape
        colors = colors.tolist()

        for x in range(loop1):
            for y in range(loop2):
                color = int(colors[x][y][0]) + int(colors[x][y][1]) + int(colors[x][y][2])
                colors[x][y].append(color)
        return colors

    def seperateColors(self, image, depth):
        image = sum(image, [])

        loops = len(image)
        colors = []

        for x in range(loops):
            color = image[x]
            if (color != 0):
                colors.append(int(color))

        if depth == 0:
            self.red = colors
            self.ColorsProcessed[0] = True
        if depth == 1:
            self.green = colors
            self.ColorsProcessed[1] = True
        else:
            self.blue = colors
            self.ColorsProcessed[2] = True

        return

    def getColors(self):
        while(True):
            if (self.ColorsProcessed[0] and self.ColorsProcessed[1] and self.ColorsProcessed[2]):
                colors = [self.red,self.blue,self.green]
                return colors

    def splitLoad(self, image):
        self.image = image
        y, x, z = self.image.shape
        image1 = []
        image2 = []
        image3 = []
        for l in range(y):
            image1.append([i[y][0] for i in self.image])
            image2.append([i[y][1] for i in self.image])
            image3.append([i[y][2] for i in self.image])

        self.ColorsProcessed = [False, False, False]

        redThread = Thread(target = self.seperateColors, args = (image1, 0))
        greenThread = Thread(target = self.seperateColors, args = (image2, 1))
        blueThread = Thread(target = self.seperateColors, args = (image3, 2))

        redThread.start()
        greenThread.start()
        blueThread.start()

        return self.getColors()

    def __init__(self):
        self.image = None
        self.ColorsProcessed = [False, False, False]
        self.colors = []
        self.red = None
        self.green = None
        self.blue = None
