
# Introduction to Artificial Neural Network & the Keras Framework
Introduction to Keras and Tensorflow with Python

Keras is a deep learning API written in Python that runs on top of TensorFlow. It is quite popular among deep learning users because of its ease of use. TensorFlow is an end-to-end open-source deep learning framework developed and maintained by Google. Similar to Numpy, TensorFlow allows for mathematical computations and manipulation between numerical tensors, runs on CPUs, GPUs, and TPUs. Keras was incorporated in TensorFlow 2.0 (the recent version) as tf.keras (high-level API) and can run on the aforementioned hardwares. TensorFlow also allows for low-level operations with the TensorFlow Core API. 

We will use the MNIST dataset to explain the concepts in the module. MNIST is a large database of handwritten digits commonly used in training and testing image processing systems. The image dimensions are 28x28 numpy arrays. Now let us import the images and prepare our dataset.

P.S: it is advisable to use Google Colab to run all the code for the content and quiz in this module.

![image](https://user-images.githubusercontent.com/93423367/210616217-bcbcb381-5e53-45ea-b00b-8f999848ec52.png)


![image](https://user-images.githubusercontent.com/93423367/210616254-0835a922-e3a6-4fa1-a0e2-9ecffd44bab8.png)


![image](https://user-images.githubusercontent.com/93423367/210616284-4396bded-1e12-4aad-b188-b674e6d7b411.png)


![image](https://user-images.githubusercontent.com/93423367/210616313-e9c919b2-affd-4581-9f47-5409c4c247ae.png)

![image](https://user-images.githubusercontent.com/93423367/210616334-db25a0ab-8257-454f-be99-964234b5b9e5.png)

![image](https://user-images.githubusercontent.com/93423367/210616385-a5ef832a-0126-4877-b639-9dc7963703fe.png)

### Multilayer perceptron

A perceptron is a supervised learning algorithm for binary classifiers that separates an input into two classes by learning linearly separable patterns. It is a single layer neural network that multiplies input feature vectors by their weights, creates a weighted sum by summing these products then adds a bias and applies an activation function to give the final output. Perceptrons are unable to solve complex problems that are not linearly separable.

![image](https://user-images.githubusercontent.com/93423367/210616502-e00b53e1-b2cb-4dc0-89e9-41c9a96fc75b.png)


![image](https://user-images.githubusercontent.com/93423367/210616515-65c16017-ce60-4200-95b6-a3b6851eb833.png)


The MultiLayer Perceptron (MLP) is a network of connected perceptrons stacked in layers with several hidden layers in between the input and output layers. When there’s a single hidden layer, MLPs are referred to as vanilla neural networks. MLPs are feedforward neural networks where information is transferred in the forward direction from the input layer to the output layer. The input data to the network is fed to the input layer, computations are performed on the data in the hidden layers and meaningful results returned in the output layer. The importance of the connections between layers is specified by the weights assigned.

![image](https://user-images.githubusercontent.com/93423367/210616575-5904685f-63d5-4019-811a-82cb11b1f8e8.png)

1. Backpropagation and its derivative

Backpropagation is the method of traversing the neural network in reverse (right to left) in order to obtain the gradient of neural network parameters with respect to a loss function. It is an iterative way of updating the weights in the network to get better predictions using a form of gradient descent until the minimum of the loss function is obtained. Different loss functions can be selected for various tasks. The loss is reduced in a controlled manner by taking small steps from the starting point to the final point which is the lowest possible point. The derivative of the loss function provides information on which direction to take when traversing. The weight can be updated using gradient descent which we will discuss later. Simply put, backpropagation involves calculating the sum of errors in the network to obtain the loss function, then the partial derivative of the loss function with respect to individual weights and using gradient descent to update the weights.

2. Activation functions and Neural Networks hyperparameters

Activation functions introduce non-linearity into the output of a neuron in a network to determine the output. This nonlinearity allows for the network to learn complex relationships between the input and response variables. Without activation functions in an artificial neural network, there will only be linear transformations on the input. The non-linear functions also allow for backpropagation because the gradients are obtained by the derivatives of the functions and used in updating weights. Some activation functions commonly used include sigmoid, tanh, relu, softmax, leaky relu and many more. When training the neural network, it is important to select the appropriate hyperparameters to improve the performance of the model.

These are some of the hyperparameters:

- Hidden layers: this is a measure of the learning capacity of the model. The more hidden layers of neurons present in the network, the better the learning capacity of the model. When too many layers than necessary are provided in a model, there is a tendency for overfitting to occur.
- Learning rate: this controls how fast the model weights are updated before reaching optimal values. With a very small learning rate, it will take the model a long time to reach the desired weights. In contrast, if the learning rate is much higher, the model might overshoot and pass the optimal point and prevent convergence of the algorithm. This rate is how fast gradient descent is performed for backpropagation.
- Dropout: this is used to shut a percentage of the neurons in the network to prevent overfitting
- Batch size: the number of data samples that can be propagated through the network before weights are updated. This is important in breaking up huge datasets into sizable batches to manage resources. For a dataset with 1000 samples, and a batch size of 100, this means that there are 10 batches.
- Epoch: it is the number of cycles that the learning algorithm goes through the entire dataset. When all batches are fed once, an epoch is completed.

![image](https://user-images.githubusercontent.com/93423367/210616735-1e341f2c-c0e2-4df0-b56b-053d4a4a1a7d.png)
