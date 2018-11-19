
# Custom-Object-Detection
Introduction to objection detection using YOLO

# YOLO - Deep Learning
This is the final phase of you yolo series journey
In this phase we are going to train the model to detect people wearing hat and people not wearing hats
Similar approach can be used to detects people wearing helemts for bike riders or construction workers wearing hats and so on.

## Selecting the number of objects to be detected
So the First step is to define the total number of clases for our model
In our example we have considered 3:
```
1. hats : Detect people with hats
2. no_hats: Detect people without hats
3. Person: Detect people
```

## Create a New .cfg file

Once we have decided the total number of classes we need to create a new cfg file.
Make a copy of the tiny-yolo.voc.cfg file in the darkflow/bin folder
Rename it to tiny-yolo-voc-3c.cfg, note: 3c indicates 3 Classes.
Open the file in notepad update the classes values to 3 in the "[region]" section.
Update the filter value to 40 in the "[configuration]" section.
Formula: 5*(classes+5) 

## Collecting the images

There are many ways to collect the dataset for training the model
The easiest way I found was by downloading through a chrome extension called ZIP images or Download all images
This plugin downlaods all the images loaded in a webpage
So, If you load about 1000 images in the google images, one click zips them all and downloads in one go

## Annotating the images

This is the most boring part of Machine learning "Annotating the images!"
There are some tools that makes our life easier but still annotating 1000's of images is time consuming and boring.
The best tool I found is Labelbox, its a online annotation tool, we can upload all the images annotate and download the xml files for training.


To be continued.. 



