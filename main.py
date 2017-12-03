import sys
import os
import importlib
import time
from time import sleep
from picamera import PiCamera
from picamera.array import PiRGBArray
import datetime

importlib.reload(sys)

import cv2

def find(x):
    imagepath = r'./'+str(x)+'.jpg'
    print(imagepath)
    start = time.clock()
    # 获取训练好的分类器参数数据
    target_cascade = cv2.CascadeClassifier(r'./cascade2.xml')
    
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

def work():
    
    camera = PiCamera()
    camera.resolution = (400,304)
    camera.framerate = 32
    rawCapture = PiRGBArray(camera, size=(400,304))
    time.sleep(1)
    target_cascade = cv2.CascadeClassifier(r'./cascade1.xml')
    # capture frames from the camera
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
        image = frame.array
	# show the frame
	
        start = time.clock()
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
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
           cv2.circle(image,((int)((x+x+w)/2),(int)((y+y+h)/2)),(int)(w/2),(0,255,0),2)
           if (x>150 and x<250 and y>150 and y<300):
               os.system('mplayer test.mp3')
               print(x,y)
               continue
               
        cv2.imshow("Find Target!",image)
        #cv2.imshow("Frame", image)
        key = cv2.waitKey(1) & 0xFF
	# clear the stream in preparation for the next frame
        rawCapture.truncate(0)
	# if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break

if __name__ == '__main__':
    work()
