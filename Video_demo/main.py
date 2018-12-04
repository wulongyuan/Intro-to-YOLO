import cv2
from darkflow.net.build import TFNet
import numpy as np
import os   
import datetime
import time
import threading 


option = {
    'model': 'cfg/tiny-yolo-voc-3c.cfg',  # Model to load
    'load': -1,                           # Weights to load
    'threshold': 0.4,                     # Threshold value, Confidence level of the object detected
    'gpu': 0                              # GPU value (0 - 1)      if tensorflow GPU is installed   
}

video_source='camera'


def write_data(result):                 # Storing the details of the objects detected in a text file
    f=open("log.txt",'a+')              # Objects detected storing in a text file for now, later updates will store in database (MangoDB)
    for i in results:
        f.write(str(datetime.datetime.now())+','+i['label']+','+str(i['confidence'])+','+str(i['topleft']['x'])+','+str(i['topleft']['y'])+','+str(i['bottomright']['x'])+','+str(i['bottomright']['y'])+','+video_source+'\n')
        f.close

tfnet = TFNet(option)
capture = cv2.VideoCapture("junk/1 (9).mp4")        # Place your path to your video file, or assign 0 to load webcam feed.
fourcc = cv2.VideoWriter_fourcc(*'XVID')            # Comment this line if you dont want to save the output video

initial_thread_count = threading.enumerate()        # Checking the current thread count
# print(len(initial_thread_count))
while (capture.isOpened()):                         # Checking if the video sources is generating frames
    stime = time.time()                             # Current time to record in the database
    ret, frame = capture.read()                     # Splittting the video feed into frames
    if ret:
        thread_count = threading.enumerate()        # Checking the latest thread count
        results = tfnet.return_predict(frame)       # Frame is sent to tfnet which intern returns a list of objects detected in the frame
        if (len(thread_count)==len(initial_thread_count)):
            threading.Timer(5.0, write_data,args=(results,)).start()    
        for result in results:                      # Loop throught the list of objects detected in the current frame
            if(result['label']=='Person'):
                frame = cv2.rectangle(frame, (result['topleft']['x'], result['bottomright']['y']), (result['bottomright']['x'], result['bottomright']['y']+30), (0,255,255),3, cv2.FILLED)
            else:
                cv2.line(frame,(result['topleft']['x'], result['topleft']['y']),(result['topleft']['x']+15, result['topleft']['y']),(0,255,255),4)
                cv2.line(frame,(result['topleft']['x'], result['topleft']['y']),(result['topleft']['x'], result['topleft']['y']+15),(0,255,255),4)
                cv2.line(frame,(result['topleft']['x'], result['bottomright']['y']),(result['topleft']['x']+15, result['bottomright']['y']),(0,255,255),4)
                cv2.line(frame,(result['topleft']['x'], result['bottomright']['y']),(result['topleft']['x'], result['bottomright']['y']-15),(0,255,255),4)
                
                cv2.line(frame,(result['bottomright']['x'], result['bottomright']['y']),(result['bottomright']['x']-15, result['bottomright']['y']),(0,255,255),4)
                cv2.line(frame,(result['bottomright']['x'], result['bottomright']['y']),(result['bottomright']['x'], result['bottomright']['y']-15),(0,255,255),4)
                cv2.line(frame,(result['bottomright']['x'], result['topleft']['y']),(result['bottomright']['x']-15, result['topleft']['y']),(0,255,255),4)
                cv2.line(frame,(result['bottomright']['x'], result['topleft']['y']),(result['bottomright']['x'], result['topleft']['y']+15),(0,255,255),4)

                frame = cv2.putText(frame, result['label'],((result['topleft']['x']),(result['bottomright']['y'])+30), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,0), 1)
                
        cv2.imshow('frame', frame)      # Display the output for each frame
        #out.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        capture.release()
        cv2.destroyAllWindows()
        break
