import numpy as np
import cv2
img = cv2.imread('samples/image1.jpg');
im2 = img.reshape((-1,3))
im2 = np.float32(im2);

k = 5;
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
ret,label,center = cv2.kmeans(im2,k,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS);
center = np.uint8(center);
res = center[label.flatten()]
res2 = res.reshape((img.shape))
res2 = cv2.medianBlur(res2,5);
cv2.imshow('res2',res2)
cv2.waitKey(0)
cv2.destroyAllWindows()
