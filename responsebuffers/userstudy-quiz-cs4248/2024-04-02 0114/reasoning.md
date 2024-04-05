Mini-batch gradient descent offers a computationally efficient way to estimate the gradient and update weights in neural networks, particularly important in NLP where datasets can be large and full gradient computation is expensive. This method provides a practical balance between the expensive computation of batch gradient descent (where the entire dataset is used to compute a gradient) and the high variance updates of stochastic gradient descent (where a single data point is used). The choice of the size of the mini-batch allows for flexibility in managing the trade-off between computational resource usage and the convergence stability, making it a widely adopted approach in training neural networks for NLP tasks.