#coding:utf-8
import random
from math import cos, sin, pi
from PIL import Image, ImageDraw

points = 512
centerX = centerY = 500
minRad = 10
maxRad = 13
Rad = 10

background = Image.new('RGBA',(1440,900),(255,255,255,255))
draw = ImageDraw.Draw(background)

"""
这部分利用分形法对图形进行分割
"""
class Node:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.next = None

iters = 5

firstPoint = Node(0,1)
lastPoint = Node(1,1)
firstPoint.next = lastPoint
minY = maxY = 1

for i in range(iters):
    point = firstPoint
    while(point.next != None):
        nextPoint = point.next

        dx = nextPoint.x - point.x
        newX = 0.5 * (point.x + nextPoint.x)
        newY = 0.5 * (point.y + nextPoint.y)
        newY += dx * (random.random() * 2 - 1)

        newPoint = Node(newX, newY)

        if(newY < minY):
            minY = newY
        elif (newY < maxY):
            maxY = newY

        newPoint.next = nextPoint
        point.next = newPoint
        point = nextPoint

normalizeRate = 1 / (maxY - minY)
point = firstPoint
while(point != None):
    point.y = normalizeRate * (point.y - minY)
    point = point.next


theta = 0;

point = firstPoint
theta = 0
pointlist = []
while(point != None):
    theta = 2 * pi * point.x
    rad = minRad + point.y * (maxRad - minRad)
    x = centerX + rad * cos(theta)
    y = centerY + rad * sin(theta)
    pointlist.append((x,y))
    point = point.next

points = len(pointlist)
for i in range(len(pointlist)):
    draw.line((pointlist[i][0],pointlist[i][1],
        pointlist[(i+1)%points][0],pointlist[(i+1)%points][1]),fill=44)

background.show();