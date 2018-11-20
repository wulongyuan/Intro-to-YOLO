
# Custom-Object-Detection
Introduction to object detection using YOLO

# YOLO - Deep Learning
This is the final phase of our journey in the yolo series. 
In this phase we are going to train the model to detect people wearing hat and people not wearing hats
Similar approach can be used to detects people wearing helemts for bike riders or construction workers wearing hats and so on.

## Lets GO!

![alt text](https://github.com/santoshmn26/Intro-to-YOLO/blob/master/Custom-Object-Detection/github.gif)

## Step 1:

Create a new folder, open the new folder, now hold shift and then right click and select open command window here to open the cmd in current path and execute the following commands.

Clone the darkflow repository
```
git clone https://github.com/thtrieu/darkflow
```
Now build the files, before building make sure cython is installed
To install Cython, skip if already installed Cython
```
pip install Cython
```
Move into darkflow directory
```
cd darkflow
```
```
python3 setup.py build_ext --inplace
```

## Step 2:

### Selecting the number of objects to be detected
So the First step is to select the total number of clases for our model. i.e Total number of objects to be detected.

In our example we have considered 3:

```
1. hats : Detect people with hats
2. no_hats: Detect people without hats
3. Person: Detect a person
```

## Step 3:

### Create a New .cfg file
Once we have decided the total number of classes we need to create a new cfg file.

Go to darkflow/cfg folder 

Make a copy of the tiny-yolo.voc.cfg file 

Rename it to tiny-yolo-voc-3c.cfg, note: 3c indicates 3 Classes.

Open the file in notepad update the classes values to 3 in the "[region]" section.

Update the filter value to 40 in the "[configuration]" section.

Formula: 5*(classes+5) 

### labels.txt

edit the labels.txt file in the darkflow directory add the following content
```
hat
no_hat
person
```

### Download the tiny-yolo-voc.weights file

Download the tiny-yolo-voc.weights file from here. [https://github.com/leetenki/YOLOtiny_v2_chainer/blob/master/tiny-yolo-voc.weights] 

## Step 4:

### Collecting the images

There are many ways to collect the dataset for training the model.

The easiest way I found was by downloading through a chrome extension called ZIP images or Download all images

This plugin downlaods all the images loaded in a webpage. So, If you load about 1000 images in the google images, one click zips them all and downloads in one go

Next we need to filter out unwanted images from the dataset.


## Annotating the images

This is the most boring part of Machine learning "Annotating the images!"

There are some tools out there that makes our life easier but still annotating 1000's of images is time consuming.

Some of the best tools I have found so far
```
1. LabelBox [https://www.labelbox.com/]
2. LabelImg [https://tzutalin.github.io/labelImg/]
```

## Step 5

### Lets start training!

To train a Neural network we need a lot of hardware power, we need good GPU like 1070 Ti or K80's for training faster or it can take hours.

### Google Colla

Google always has a solution!

Google provides a free service with 12GB of free GPU for training neural networks for research work.

Go to google colab and register with a google account.

Go to edit/notebook settings and select GPU in Hardware accelerator.

Next click on connect and select hosted run time in the top right corner.

### Prepare the files

Next in the local system zip the following files and name it as darkflow-master_annotation_4.0.zip (optional)
```
1. Dataset foleder: folder with images
2. Annotation folder: folder with xml files
3. tiny-yolo-voc-3c.cfg: cfg file from darkflow/cfg 
4. tiny-yolo-voc.weights: weights file from darkflow/bin 
5. labels.txt: labels file
```

### Upload the files to google colab

Click on the > key on the left side to open the contents tab, now select Files

Now click on upload and upload the zip file

Next follow the steps here. [https://github.com/santoshmn26/Intro-to-YOLO/blob/master/Google%20Colab/training_dataset.ipynb]

Execute the commands one by one.

After about 100 epoch if the moving avg loss is less than 5% stop the execution    

go to ckpt folder download the latest files
```
1. .meta
2. .index
3. .profile
4. .data
5. checkpoing
```

### Testing the model

Now place the downloaded files in darkflow/ckpt folder

Note: Create the ckpt folder if not present already

Now run the main.py file in the darkflow folder using command prompt

```
python main.py
```






