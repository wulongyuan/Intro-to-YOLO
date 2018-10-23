# Testing the yolov3 model on images.

In this project we use the pre-trained yolov3 model to detect objects in a picture
For this projects we are using the images available in the dark-master/sample_img dir.
Note: You can place your own image to test the model too. 
For simplicty, to cycle through the images in the folder lets rename the images in the folder.

Open powershell in the dark-master/sample_img dir and enter the following command
```
Dir | %{Rename-Item $_ -NewName ("Image_{0}.jpg" -f $nr++)}
```

This converts all the file names of the files in the folder dark-master/sample_img to 
```
- Image_0
- Image_1 
- ....
- ....
- Image_n
```
