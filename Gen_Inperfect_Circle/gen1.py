#coding:utf-8
import random
from math import cos, sin, pi
from PIL import Image, ImageDraw

points = 512
centerX = centerY = 500
minRad = 20
maxRad = 40
Rad = 20

background = Image.new('RGBA',(1440,900),(255,255,255,255))
draw = ImageDraw.Draw(background)

theta = 0;
pointlist = [];
for i in range(points):
    rad = minRad + random.random() * (maxRad - minRad)
    x = centerX + rad * cos(2*pi*i/points)
    y = centerY + rad * sin(2*pi*i/points)
    pointlist.append((x,y))

for i in range(points):
    draw.line((pointlist[i][0],pointlist[i][1],
    	pointlist[(i+1)%points][0],pointlist[(i+1)%points][1]),fill=44)

background.show();