import cv2
from darkflow.net.build import TFNet
import numpy as np
import os   
import datetime
import time

option = {
    'model': 'cfg/yolov3.cfg',      # The pre-trained yolo model
    'load': bin/yolov3.weights,                             # Weights file
    'threshold': 0.1                          # threshold value
}

tfnet = TFNet(option)
capture = cv2.VideoCapture('videofile.mp4')   # Video source file
colors = [tuple(255 * np.random.rand(3)) for i in range(10)]
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.mp4',fourcc, 20.0, (640,480))
while (capture.isOpened()):
    ret, frame = capture.read()
    if ret:
        results = tfnet.return_predict(frame)
        for color, result in zip(colors, results):
            if(result['confidence']<0.5):   # Confidence level of 50%
                continue
            else:
                tl = (result['topleft']['x'], result['topleft']['y'])
                br = (result['bottomright']['x'], result['bottomright']['y'])
                frame = cv2.rectangle(frame, tl, br, color, 7)
                frame = cv2.putText(frame, label, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        capture.release()
        cv2.destroyAllWindows()
        break
