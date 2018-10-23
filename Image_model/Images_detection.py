import cv2
from darkflow.net.build import TFNet
import matplotlib.pyplot as plt
import numpy as np


options = {
    'model': 'cfg/yolov3.cfg',                                                              # yolo pre-trained model
    'load': bin/yolov3.weights,                                                             # yolov3 weights
    'threshold': 0.15
}

tfnet = TFNet(options)
i=75
colors = [tuple(255 * np.random.rand(3)) for i in range(10)]
for i in range(76,300):
    try:
        img_path="C:\\path\\image"+str(i)+".jpg"                                            #Change the path
        img = cv2.imread(img_path, cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = tfnet.return_predict(img)
        for color, result in zip(colors, results):
            print(result['label'],"{:.2f}".format(result['confidence']*100))
            if(result['confidence']<0.1):
                continue
            else:
                tl = (result['topleft']['x'], result['topleft']['y'])
                br = (result['bottomright']['x'], result['bottomright']['y'])
                label = result['label']
                img = cv2.rectangle(img, tl, br, color, 7)
                img = cv2.putText(img, label, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
        plt.imshow(img)
        plt.show()
        print('----------------------------------')
    except:
        continue
