# Tiny-YOLOv3

For this tutorial we are going to work on Tiny-Yolo a simple version of YOLO model
There are various versions of YOLO each having their own features such as FPS, Flops, cfg and weights files.
![alt text](https://www.arunponnusamy.com/images/yolo-object-detection-opencv-python/yolo-object-detection.jpg)

## Some of the latest versions include:

| Model	           | Train	        | Test	    | mAP	    | FLOPS	    | FPS	|  
|------------------|----------------|-----------|-----------|-----------|-------| 
| SSD300	       | COCO trainval  | test-dev	| 41.2	    | -	        |  46	|    
| SSD500	       | COCO trainval	| test-dev	| 46.5	    | -	        |  19	|   
| YOLOv2 608x608   | COCO trainval	| test-dev	| 48.1	    | 62.94 Bn	|  40	|    
| Tiny YOLO	       | COCO trainval	| test-dev	| 23.7	    | 5.41 Bn	|  244  |	
| SSD321	       | COCO trainval	| test-dev	| 45.4	    | -	        |  16	|    
| DSSD321	       | COCO trainval	| test-dev	| 46.1	    | -	        |  12	|    
| R-FCN	           | COCO trainval	| test-dev	| 51.9	    | -	        |  12	|    
| SSD513	       | COCO trainval	| test-dev	| 50.4	    | -	        |  8    | 	
| DSSD513	       | COCO trainval	| test-dev	| 53.3	    | -	        |  6	|    
| FPN FRCN	       | COCO trainval	| test-dev	| 59.1	    | -	        |  6	|    
| Retinanet-50-500 | COCO trainval	| test-dev	| 50.9	    | -	        |  14	|    
| Retinanet-101-500|COCO trainval	| test-dev	| 53.1	    | -	        |  11	|    
| Retinanet-101-800|COCO trainval	| test-dev	| 57.5	    | -	        |  5	|    
| YOLOv3-320	   |COCO trainval	| test-dev	| 51.5	    | 38.97 Bn	|  45	|    
| YOLOv3-416	   |COCO trainval	| test-dev	| 55.3	    | 65.86 Bn	|  35   |	
| YOLOv3-608	   |COCO trainval	| test-dev	| 57.9	    | 140.69 Bn	|  20	|
| YOLOv3-tiny	   |COCO trainval	| test-dev	| 33.1	    | 5.56 Bn   |  220	|
| YOLOv3-spp	   |COCO trainval	| test-dev	| 60.6	    | 141.45 Bn	|  20	|

## Pre-requirements

```
1. Python 3.5+ or anaconda python 3.5+.
    - preferred Anaconda python because it contains various packages pre-installed which is required for this project
    
2. Tensorflow GPU or Tensorflow CPU 
    - Preferred Tensorflow GPU higher performance compared to Tensorflow CPU.
    
3. OpenCV for Computer Vision.
    - Downlaod the latest version [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/).
    
4. Dark-Flow Repository.
    - Dowload the Dark-Flow GitHub repo from [here](https://github.com/thtrieu/darkflow).
    
5. Model with weights for tiny-Yolov3.
    - Download the cfg file and the weights [here](https://pjreddie.com/darknet/yolo/)

6. Download a sample video file containing some common objects such as cars, cats, dogs and so on.
```

## Testing the model

1. Extract the Repository to a folder.

2. Build the model 
```
    - open cmd and type "python setup.py build_ext --inplace"
```
   
3. Place the downloaded .weights file in the bin folder and .cfg file in the cfg folder.

4. Place the downloaded video file in the Dark-Flow directory (extracted folder) and rename it to videofile.mp4.

5. Open Command prompt and enter the following command.
```
    - python flow --model cfg/tiny-yolo.cfg --load bin/yolov3.weights --demo videofile.mp4 --gpu 1.0 --saveVideo
```

## Code breakdown
```
1. Python - Indicates to use Python packages.

2. flow - Initiate the dark-flow files

3. --model - tag used to specify the model which we are using to detect the objects in the videofile

4. cfg/tiny-yolo.cfg - Indicating to use the downloaded pre-trained model to detect objects in the video.

5.  --load - tag used to specify the weight values of the the neural network for the trained model.

6. --demo - tag used to specify the video file to undergo object detection.

7. --gpu - tag used to specify to use tensorflow gpu version instead of cpu version.
    Note: you can ommite the --gpu if you are using cpu version of tensorflow.
 
8. 1.0 - indecates to use 100% of gpu to perform object detection using the specified model.

9. --saveVideo - tag used to save the output video.
```

