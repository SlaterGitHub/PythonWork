from threading import Thread
import MergeSort as ms
import numpy as np

class ColorSplitter:
    def proportionColors(self, colors):
        const = colors[0][3]
        for x in range(len(colors)):
            colors[x][3] += -(const)

        return colors
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
        while(y < len(colors)):
            while(x < len(colors[y])-1):
                if (colors[y][x][0] == colors[y][x+1][0]) and (colors[y][x][1] == colors[y][x+1][1]) and (colors[y][x][2] == colors[y][x+1][2]):
                    colors[y].pop(x+1)
                    z+=1
                else:
                    colors[y][x].append(z)
                    z=1
                    x+=1
            colors[y][x].append(1)
            y+=1
            x=0
        return colors

    def sortColors(self, colors):
        colors = sorted(colors, key=lambda y: y[3])

        return colors

    def addIndexes(self, colors, run):
        for x in range(len(colors)):
            colors[x].append(x+1)

        return colors

    def addColors(self, colors):
        loop1, loop2, d = colors.shape
        colors = colors.tolist()

        for x in range(loop1):
            for y in range(loop2):
                color = round((int(colors[x][y][0]) + int(colors[x][y][1]) + int(colors[x][y][2]))/3)
                colors[x][y].append(color)
        return colors
