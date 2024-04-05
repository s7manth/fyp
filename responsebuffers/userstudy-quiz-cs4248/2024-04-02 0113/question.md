Consider the problem of training a feedforward neural network to perform sentiment analysis on movie reviews. Given a dataset consisting of reviews labeled as either "positive" or "negative", you decide to use a simple feedforward neural network with a single hidden layer. This network utilizes sigmoid activation functions for the hidden layer neurons and a softmax output layer for classification. You initialize the network with small random weights and start training. After several epochs, you notice that the training loss decreases as expected, but the validation loss does not decrease and stays more or less constant. What could be the most likely reason for this observation?

1. The learning rate is set too high, causing the weights to diverge.
2. The network is too simple and is underfitting the training data.
3. There is a large amount of noise in the dataset that affects validation more than training.
4. Dropout was not applied, leading to overfitting on the training data.
5. The softmax function is inappropriate for a binary classification task.