import cv2
import numpy as np
from pyzbar.pyzbar import decode
import datetime

def qrScanner():
    cap = cv2.VideoCapture(1)
    cap.set(3, 640)
    cap.set(4, 480)
    
    while True:
        success, img = cap.read()
        for qr in decode(img):
            data = qr.data.decode('utf-8')
            #this is for checking if qr is being scanned
            print(data)
            x = str(datetime.datetime.now())
            print(x)
            date = x[0:11]
            time = x[11:19]
            with open('info.txt', 'w') as f:
                f.write(data)
            with open('info.txt', 'a') as f:
                f.write(f"date created: {date}")
                f.write("\n")
                f.write(f"time created: {time}") 
        cv2.imshow('frame', img)
        cv2.waitKey(1)

qrScanner()
    
    
    


