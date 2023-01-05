# Regularization & Optimization
Common regularization for deep learning

 In previous modules, we have discussed regularisation and how it prevents overfitting in models. In deep learning, models are also susceptible to overfitting. As a result, different techniques have been developed to prevent overfitting. L1 & L2 regularization, dropout, data augmentation and early stopping are some regularization methods.

- Dropout: this is a frequently used technique in deep learning where units are ignored (“dropped out”) in a neural network. A percentage of the neurons in each layer in the network are randomly selected and ignored such that they do not make any contribution in the forward and backward pass. This automatically results in a much smaller network where the neurons left are required to handle the representations that would have been used for predictions by the missing neurons by learning more robust features. This process improves the generalization capabilities of the network and reduces overfitting on the training data.

![image](https://user-images.githubusercontent.com/93423367/210821412-beab58bf-d49b-4493-bfd7-0b9292661f95.png)

- Early stopping: when a model is trained for a longer period such that the validation error starts to increase, overfitting is said to occur. In early stopping, while fitting the model on the training data and evaluating on the validation set, when the validation error stops reducing or gets worse, the training process is terminated before the lowest training error is obtained to prevent overfitting.
- Data augmentation: training the model on a larger dataset is another way to prevent overfitting. Data augmentation involves increasing the size of the training set by introducing minor changes like rotating, cropping, flipping, translating, blurring to generate synthetic data from the dataset. 

Optimisation for training deep neural networks

When solving deep learning problems, a loss function is defined to minimize the loss using an optimisation algorithm like gradient descent, gradient descent with momentum, Adagrad, RMSProp, Adam and others. While there are several optimisation algorithms, there are also some challenges such as local minima, saddle points, vanishing gradients etc faced in deep learning optimisation. 

Local minima: neural networks aim to continue updating weights until the global minimum (the lowest point of the entire network) is attained. Local minima refer to the lowest points of localised portions of the graph. The value of a loss function is minimum at a point in the local region. It is possible for the function to be stuck at a local minimum because it is the best point in that locality which makes it difficult to reach the global minimum where the lowest loss can be achieved. 

Vanishing gradients: this is a problem that occurs when training a network using gradient descent methods. Vanishing gradients make it difficult to update the weights in the earlier layers of the network and worsens as the number of layers increases. As we know, with gradient descent, the gradient controls how much learning happens in the network while training. While backpropagating in deep neural networks, the gradients tend to get smaller and with small gradients, little or no learning is done hence, resulting in poor performance of models.

Although we have only discussed some of the challenges in deep learning optimisation at a high level, we will now discuss some optimisation algorithms.

Gradient descent: this is a common and established optimisation algorithm used to obtain the minimum of an objective function J using the negative of the gradient to continuously move towards the steepest point. It can be likened to finding the lowest point of a mountain. Gradient descent can be summed up with the equation below:

![image](https://user-images.githubusercontent.com/93423367/210821655-c2e2e337-a45e-4c91-9649-f6bce0683632.png)

Batch gradient descent, stochastic gradient descent and mini-batch gradient descent are the three variants of gradient descent. Which variant to be used is determined by the size of data available.

![image](https://user-images.githubusercontent.com/93423367/210821726-5fc7e90c-aaa2-4ee1-90e1-a6f5db224010.png)


Batch gradient descent computes the gradient of the cost function with the entire training set, faster than batch, stochastic gradient descent (SDG) uses each sample in the training set to perform updates at a time. Mini-batch gradient descent combines the logic of other variants by using only mini-batches of training examples to update weights. It allows for a stable convergence because the variance of the parameter updates are also reduced.

Gradient descent with momentum: similar to gradient descent, the addition of momentum to the algorithm helps speed up convergence by accelerating the gradient vectors in the correct direction. With gradient descent, movement is not always in the optimal direction however, gradient descent with momentum oscillates in the right direction by considering past gradients and computing exponentially weighted averages of the gradients which are used to update the weights.

Adagrad - Adaptive Gradients: adagrad changes the learning rate for every update by tracking the sum of gradient squared and uses it to adjust the gradients in the right direction. Larger updates are performed for infrequent parameters with high learning rates while smaller updates are performed for frequent parameters with low learning rates. This can be interpreted as “the more a parameter is updated, the less updates are required for the parameter in future updates to allow for the updates of other parameters”. This makes it a suitable choice for sparse data.

RMSProp - Root Mean Square Propagation: although similar to Adagrad, RMSProp provides an exponentially decaying average as opposed to the sum of the gradients by Adagrad. It changes the learning rate slower and converges faster than Adagrad by using a decay rate to consider the gradients of recent time steps.

Adam - Adaptive Moment Estimation: this algorithm uses the first and second moments of gradients when adapting the learning rate for each weight of the neural network. It can be likened to RMSProp with momentum such that exponential moving averages of gradients are calculated then squared. It also benefits from the advantages of Adagrad such that it works well with sparse gradients.

![image](https://user-images.githubusercontent.com/93423367/210821825-b78071ad-3165-478e-8d7d-5aca778b817d.png)

![image](https://user-images.githubusercontent.com/93423367/210821873-0b219674-9932-4a3a-b8b9-8dab7db7094f.png)

![image](https://user-images.githubusercontent.com/93423367/210821897-e8fcdbe1-bdfc-4001-9dda-016b9f23e2c2.png)
