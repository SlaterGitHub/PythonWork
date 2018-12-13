import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import UnivariateSpline

def Vector(x1, x2, y1, y2, t):
    t = float(t) *0.0002
    return int(x1 + (x2-x1) * g), int(y1 + (y2-y1) * g)

times = []
rows = []
Rline = []
Tline = []
time = None
row = None
data = None

data = open("SortTimes.txt", "r").readlines()

for x in range(len(data)):
    time, row = data[x].split(',')
    time = float(time)
    time = int(time*1000)
    times.append(time)
    row = int(row)
    rows.append(row)

vectorX = [rows[0], rows[(len(rows)/2)], rows[len(rows)-1]]
vectorY = [times[0], times[(len(times)/2)], times[len(times)-1]]

for g in range(5000):
    vx1, vy1 = Vector(vectorX[0], vectorX[1], vectorY[0], vectorY[1], g)
    vx2, vy2 = Vector(vectorX[1], vectorX[2], vectorY[1], vectorY[2], g)
    v1, v2 = Vector(vx1, vx2, vy1, vy2, g)
    Rline.append(v1)
    Tline.append(v2)

plt.plot(rows, times, 'o')
#plt.plot(Rline, Tline)

plt.show()

    

