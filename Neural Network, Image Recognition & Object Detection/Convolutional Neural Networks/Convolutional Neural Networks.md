In this lesson, you will learn about convolutional neural networks and how they are used in deep learning to analyze visual imagery.

Motivations

Convolutional neural network also known as ConvNets or CNN is a class of deep, feed-forward artificial neural networks specifically designed for image input. As a result of their performance as opposed to traditional fully-connected neural networks, CNNs have been widely applied in computer vision tasks such as image recognition, image classification, object detection etc. More recently, they are being explored in the natural language processing domain by researchers. To put simply, we can teach computers to “see” using CNNs. An image is a grid of numbers that represent pixel values which are interpreted as a matrix of values by a computer.  The convolution operation that occurs in a CNN network allows for sparse representation of inputs by only concentrating on the relevant features as opposed to using a regular neural network which will increase the number of computations by performing matrix multiplications. Additionally, parameter sharing in CNNs saves memory by using the same weight parameters for all neurons in the same feature map.  

1.Convolution operator

2.Layers, filters, pooling and feature maps
Convolutional layer, pooling layer and fully-connected layer are the three main types of layers used to build the CNN architecture.

Convolutional layer: This is the building block of CNNs. In mathematics, convolution refers to a mathematical operation on two functions to create a third function. Unsurprisingly, from the name, a convolution operator is used to extract features such as colour, edges orientation etc from input images in CNNs. It learns the image features using small squares of the input data to preserve the relationships between pixels.  A convolution is performed on the input data using a filter or kernel to produce a feature map. By including more layers, the network is able to learn more high-level features and have a better understanding of the images and better identifies unseen images. Considering a 5x5 image matrix with pixel values 0 and 1 and a 3x3 filter matrix, the convolution of both matrices result in a feature map as shown below

![image](https://user-images.githubusercontent.com/93423367/211045747-2334bfcd-3809-47ab-89cc-4682711d67da.png)

We slide the filter matrix over the feature matrix by a set number of pixels and perform an element wise multiplication for each position. It is important to note that different filters perform different operations by acting as feature detectors from the original images. The number of pixels or size of step the filter moves over is known as stride. To introduce non-linearity, a relu activation is applied after every convolution operation in the convolutional layer

Pooling layer: this is the layer periodically inserted in-between successive convolution layers where dimensionality reduction is performed by pooling. Pooling (also called downsampling) helps to control overfitting, train faster and reduce the number of parameters and computations in the network. Although this reduces dimensionality, the important information is still retained. Maximum, average and sum pooling are different types of pooling with max commonly used. Max pooling takes the maximum element from the feature map.

![image](https://user-images.githubusercontent.com/93423367/211045819-d483315d-13c9-4488-8d37-ccfbf0fc9fdf.png)

Fully connected layer: the features extracted from the convolution and pooling layers are fed into the fully connected layer to use for classification into different classes in the training set and also learning the non-linear combinations of the features since it is possible to obtain even better results with a combination of the features. Softmax is used as the activation function to obtain probabilities of the different classes which sum to 1.

Combining the layers described, for a CNN, an input image is provided for the convolution layer, filters are applied with strides to perform convolution, pooling is done for dimensionality reduction, more convolution and pooling layers can be added, the output of these layers is fef into a fully-connected layer and an activation function applied to obtain final probabilities for the classes.

![image](https://user-images.githubusercontent.com/93423367/211045886-795fffac-59a2-4bdf-993a-d823b8b876d3.png)




