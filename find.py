# coding:utf-8

import sys
import importlib
import time

importlib.reload(sys)

import cv2

# 待检测的图片路径

imagepath = r'./heat.jpg'

 
start = time.clock()

# 获取训练好的分类器参数数据

target_cascade = cv2.CascadeClassifier(r'./cascade1.xml')

 

# 读取图片

image = cv2.imread(imagepath)

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

 

# 探测图片中的目标

target = target_cascade.detectMultiScale(

    gray,

    scaleFactor = 1.15,

    minNeighbors = 5,

    minSize = (5,5),

    # flags = cv2.cv.CV_HAAR_SCALE_IMAGE

)

 
elapsed = (time.clock() - start)
print("detect Time used:",elapsed)
print("发现{0}个目标!".format(len(target)))

 

for(x,y,w,h) in target:

    # cv2.rectangle(image,(x,y),(x+w,y+w),(0,255,0),2)

    cv2.circle(image,((int)((x+x+w)/2),(int)((y+y+h)/2)),(int)(w/2),(0,255,0),2)

 

cv2.imshow("Find Target!",image)

cv2.waitKey(0)

