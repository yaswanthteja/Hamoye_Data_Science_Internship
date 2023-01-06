Introduction to Large Scale Image Recognition Architecture
Over time, numerous CNN architectures have been developed, most of which follow the fundamental method of applying convolution layers to the input and periodically downsampling.

In this lesson, we will briefly discuss some of these architectures.

Over time, numerous CNN architectures have been developed, most of which follow the fundamental method of applying convolution layers to the input and periodically downsampling. In this section, we briefly discuss some of these architectures. 

Image Net

ImageNet is a large image dataset commonly used for research with the images labelled and organised by hierarchy. The dataset contains more than 14 million images labelled into over 20,000 categories. ImageNet Large Scale Visual Recognition Challenge (ILSVRC) is an annual competition (2010 - 2017) where computer vision algorithms especially for image classification and object detection  are evaluated  and compared using subsets of the ImageNet. The challenge aims to set state of the art results for various tasks and techniques. Some of the architectures we will discuss have proven to be successful in ILSVRC.

AlexNet, VGG, ResNet and DenseNet

AlexNet: Introduced in 2012, this network consists of 8 layers - 5 convolutional layers, 2 fully-connected layers and one fully-connected output layer won the ILSVRC challenge in 2012. Although similar to the LeNet architecture previously developed, AlexNet uses relu as the activation function as opposed to the tanh which caused the model to train about six times faster. Additionally, max pooling layers with a window size of 3x3 and a stride of 2 overlap in this architecture.

VGG - Visual Geometry Group: this was introduced by Simonyan and Zisserman in 2014. This architecture which was the second runner up for ILSVRC in 2014 is a network that is roughly twice as deep as AlexNet uses convolutions with 3x3 kernels with padding of 1, and a 2x2 max pooling matrix with a stride of 2.  It has 13 convolutional layers and 3 fully-connected layers alongside a relu activation function as in AlexNet.

ResNet - Residual Neural Network: Used in 2015 to win ILSVRC, identified that although deeper networks were performing better, they become difficult to optimise and suffer from vanishing gradients. To address these problems, skip connections were introduced in ResNet by authors from Microsoft Research with a speculation that deeper learners should be able to learn equally as shallow layers. This is a very deep network with 152 layers trained using skip connections such that the signal for a layer is included in the output of the layer located higher up.

Transfer learning and image augmentation

Transfer learning is a concept of exporting the knowledge obtained in a particular task to a new task. Using the features that an existing model learnt with a lot more data can improve generalization in a new task or setting. The motivation for transfer learning stemmed from the fact that although many supervised models require a large number of labeled data, many scenarios typically do not have this as it is time consuming and difficult to label data points.  When performing transfer learning, what, when and how to transfer are important questions that must be answered. The portion of the knowledge learnt by the source model that will be beneficial to the new model to improve performance should be identified. Also, although transfer learning is an option to use when training new models, it might not always improve performance in the new model instead, it might even contribute negatively. Finally, it is helpful to identify how the knowledge will be transferred between models using different techniques and algorithms. For example, in computer vision, pre-trained models for challenging tasks using ImageNet are readily available to be used in transfer learning. Pre-trained models are models that have been trained on large datasets regularly reused in similar domains and tasks. Pre-trained models can serve as feature extractors or even used as they are. As explained earlier, the convolution layers that receive the inputs in CNNs learn a lot of low-level features in images, more complex features learnt in the middle layers and the results of these computations are interpreted with the output layer. With a proper understanding of this, the relevant portions can be selected and integrated when creating new networks by either freezing the existing weights to prevent updates or update these weights when training the new model hence indirectly serving as a weight initialisation phase for the new model. Some of the models discussed above can be used for transfer learning in computer vision tasks.

Image augmentation in computer vision is not new in fact, it is extremely important for sparse datasets. As mentioned earlier, augmentation helps to create a larger dataset by adding noise, rotating, flipping, cropping, rotating etc the training dataset. This helps reduce overfitting and improve the model’s capacity to generalise to even unfamiliar scenarios in new unseen data.


