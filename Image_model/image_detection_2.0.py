import cv2
from darkflow.net.build import TFNet
import matplotlib.pyplot as plt
import numpy as np
import os


options = {
    'model': 'cfg/yolov3.cfg',
    'load': bin/yolov3.weights,
    'threshold': 0.15
}

tfnet = TFNet(options)
file_names=os.listdir("C:\\Users\\santo\\Downloads\\New folder (2)\\darkflow-master\\Filtered")
colors = [tuple(255 * np.random.rand(3)) for i in range(10)]
for i in file_names:
    try:
        img_path=i
        img = cv2.imread(img_path, cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = tfnet.return_predict(img)
        print(results)
        for color, result in zip(colors, results):
            print(result['label'],"{:.2f}".format(result['confidence']*100))
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
