import numpy as np
import cv2
import sys

image = cv2.imread(sys.argv[1])

#(segmented_image,labels_image,number_regions) = pms.segment(image,spatial_radius=6,range_radius=4.5,min_density = 50)
sp = 6.5  #spatial window radius
sr = 15 #color window radius
maxlevel = 5 #max level in pyramid for segmentation
dst = image;
cv2.pyrMeanShiftFiltering(image,sp,sr,dst,maxlevel);

cv2.namedWindow('img',cv2.WINDOW_NORMAL)
cv2.imshow('img',dst)

k = cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()


