import pygame, sys
from pygame.locals import *
import random

def makeCluster():

    axis = [None]*4

    for x in range(2):
        axis[x] = random.randint(0, 700)
    for x in range(2):
        axis[x+2] = random.randint(0, 600)

    cluster = []

    for x in range(axis[0]*axis[1]):
        clust = (random.randint(0, 100), 0, random.randint(0, 100))
        cluster.append(clust)

    return cluster, axis

def starLoc():
    loc = []
    for x in range(1280*720):
        loc.append(random.randint(0, 7000))

    return loc

def makeMap(loc):
    """indx = 0
    print(axis[0])
    print(axis[1])
    print(axis[2])
    print(axis[3])
    for x in range(axis[0]):
        for y in range(axis[1]):
            pygame.draw.rect(Dis, cluster[indx], (y+axis[2], x+axis[3], 1, 1))
            indx+=1"""

    indx = 0

    for x in range(1280):
        for y in range(720):
            if loc[indx] == 1:
                size = random.randint(1, 3)
                pygame.draw.rect(Dis, (255, 255, 220), (x, y, random.randint(1, 3), random.randint(1, 3)))

            indx+=1

pygame.init()

Dis = pygame.display.set_mode((1280, 720))

void = ( 0, 0, 0)
star = (255, 255, 220)
clust = (0, 0 , 0)


pygame.display.set_caption('firstGame')
cluster, axis = makeCluster()
makeMap(starLoc())

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
