#!/usr/bin/env python3
import numpy as np
import cv2
from display import Display

W = 1920//4
H = 1080//4

d = Display(W,H)

def process_frame(img):
    img = cv2.resize(img, (W,H))
    d.paint(img)
    
if __name__ == "__main__":
    cap = cv2.VideoCapture("test.mp4")
    
    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            process_frame(frame)
        else:
            break
