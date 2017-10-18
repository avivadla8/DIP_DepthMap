import cv2
import numpy as np
import sys
from matplotlib import pyplot as plt

filename = "./samples/image1.jpg"
image = cv2.imread(filename)
image_hsv = cv2.cvtColor(image,cv2.COLOR_RGB2LUV)

cv2.imshow('img',image);
dst = image;
    #decl (input,sp,sr,out,max_level)s
    #sp - spatial window radius , sr = color window radius
cv2.pyrMeanShiftFiltering(image,30,20,dst,3)
cv2.imshow('img2',dst);

med = cv2.medianBlur(dst,5);
img_hsv = cv2.cvtColor(dst,cv2.COLOR_RGB2HSV)
cv2.imshow('img3',img_hsv)

k = cv2.waitKey(0);
if(k==27):
    cv2.destroyAllWindows()

color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img_hsv],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()


