Object Detection - Multi-Object Classification plus Localization
In this lesson, you will learn about object detection, and some commonly used object detection algorithms.

Motivations and Terms

In object localisation tasks, the location of objects in images are identified and put in boundary boxes while classification assigns a label to each image. Object detection often referred to as object recognition  involves a combination of object classification and object localisation such that different objects in an image are found and classified. In object detection, the output is variable in length because the number of objects detected in different images may change. Object detection can be used for face detection as seen in some cameras, counting, visual search engines such as that of Pinterest, aerial image analysis. A problem with obtaining a variable number of objects is that it becomes difficult to obtain fixed-sized vectors; however, sliding windows computed convolutionally  are commonly used to resolve this. 

Region-based Convolutional Neural Network (R-CNN) is a well-known architecture used for object detection such that a selective search algorithm generates about 2000 region proposals which are later passed to a CNN for feature extraction. An SVM (Support Vector Machine) is used to classify objects in the region proposal then a boundary box regression used to localise objects present. Region proposals are smaller parts of the original image identified to possibly contain the objects being searched for.  Bounding box regressor uses a scale-invariant linear regression model to create bounding boxes for the objects. They learn a target transformation between the predicted proposal and the ground truth When training the model, pairs of predicted and ground truth of four localisation dimensions are used such that the predicted bounding box p = (px, py, pw, ph) with px and py as the center coordinates, pw the width and ph the height while the ground truth is g= (g, gy, gw, gh). The transformation between both boxes using the linear regressor can be represented as: ĝx =pwdx(p) + px, ĝy =phdy(p) + py, ĝw =pwexp(dw(p)), ĝh =phexp(dh(p))


![image](https://user-images.githubusercontent.com/93423367/211047682-fc571365-4967-47e6-9a4b-2e8ed015ef7c.png)


A downside of R-CNN is that it is computationally expensive and slow due to the many forward computations performed by CNNs on the proposed regions for a single image.

Another object detection algorithm that is less computationally expensive is a type of single shot detection (SSD) algorithm called You Only Look Once “YOLO”. It is a cutting-edge detection algorithm that can identify distinct objects within the space of an image. It looks at the image once, divides it into grid cells, which are responsible for predicting bounding boxes, and output a score known as the Intersection Over Union (IOU). For each bounding box, the grid cells also predict a class alongside the probability distribution over all possible classes. The class-specific confidence score is a multiplication of the individual box confidence predictions and the conditional class probabilities.

