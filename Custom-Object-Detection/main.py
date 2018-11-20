import cv2
from darkflow.net.build import TFNet
import numpy as np
import os   
import datetime
import time
import threading 

option = {
    'model': 'cfg/tiny-yolo-voc-3c.cfg',
    'load': -1,
    'threshold': 0.4
}
def write_data(result):
    f=open("log.txt",'a+')
    for i in results:
        f.write(str(datetime.datetime.now())+','+i['label']+','+str(i['confidence'])+','+str(i['topleft']['x'])+','+str(i['topleft']['y'])+','+str(i['bottomright']['x'])+','+str(i['bottomright']['y'])+','+'camera\n')
        f.close

tfnet = TFNet(option)
capture = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
colors = [tuple(255 * np.random.rand(3)) for i in range(20)]
out=cv2.VideoWriter('output_videofile.mp4',fourcc, 20.0, (640,480))


while (capture.isOpened()):
    stime = time.time()
    ret, frame = capture.read()
    if ret:
        thread_count = threading.enumerate()
        results = tfnet.return_predict(frame)
        if (len(thread_count)==12):
            print(">>>>Updating logfile!")
            threading.Timer(5.0, write_data,args=(results,)).start()    
        for color, result in zip(colors, results):
            #if(result['label']=='no_hat'):
                print(result['label'],"\t",(result['confidence']))
                #frame = cv2.rectangle(frame, (result['topleft']['x'], result['topleft']['y']), (result['bottomright']['x'], result['bottomright']['y']), color, 3)
                
                cv2.line(frame,(result['topleft']['x'], result['topleft']['y']),(result['topleft']['x']+15, result['topleft']['y']),(0,255,255),5)
                cv2.line(frame,(result['topleft']['x'], result['topleft']['y']),(result['topleft']['x'], result['topleft']['y']+15),(0,255,255),5)
                cv2.line(frame,(result['topleft']['x'], result['bottomright']['y']),(result['topleft']['x']+15, result['bottomright']['y']),(0,255,255),5)
                cv2.line(frame,(result['topleft']['x'], result['bottomright']['y']),(result['topleft']['x'], result['bottomright']['y']-15),(0,255,255),5)
                
                cv2.line(frame,(result['bottomright']['x'], result['bottomright']['y']),(result['bottomright']['x']-15, result['bottomright']['y']),(0,255,255),5)
                cv2.line(frame,(result['bottomright']['x'], result['bottomright']['y']),(result['bottomright']['x'], result['bottomright']['y']-15),(0,255,255),5)
                cv2.line(frame,(result['bottomright']['x'], result['topleft']['y']),(result['bottomright']['x']-15, result['topleft']['y']),(0,255,255),5)
                cv2.line(frame,(result['bottomright']['x'], result['topleft']['y']),(result['bottomright']['x'], result['topleft']['y']+15),(0,255,255),5)
                
                
                frame = cv2.putText(frame, result['label'],((result['topleft']['x'])+6,(result['bottomright']['y'])-6), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,0), 1)
        cv2.imshow('frame', frame)
        out.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        capture.release()
        cv2.destroyAllWindows()
        break