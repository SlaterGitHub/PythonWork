import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from numpy import ones,vstack
from numpy.linalg import lstsq
from threading import Thread

class Graph:
    def showGraph(self, x, y):
        plt.plot(x, y, 'o')
        plt.show()
        return

    def getData(self, data, index):
        return [i[index] for i in data]

    def plotData(self, data, y, x):
        Xdata = self.getData(data, x)
        Ydata = self.getData(data, y)

        displayGraph = Thread(target = self.showGraph, args = (Xdata, Ydata))
        displayGraph.start()

    def getLineEquation(self, data, y ,x):
        Xdata = self.getData(data, x)
        Ydata = self.getData(data, y)

        A = vstack([Xdata,ones(len(Xdata))]).T
        m, c = lstsq(A, Ydata)[0]
        return [m,c]
