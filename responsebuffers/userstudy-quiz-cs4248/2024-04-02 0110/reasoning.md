L2 regularization, often termed as Ridge Regularization, works by adding a penalty to the loss function that is proportional to the square of the magnitude of the coefficients. The general formula for the regularized cost function in logistic regression which incorporates L2 regularization is given by:

$$J(\theta) = -\frac{1}{m}[\sum_{i=1}^{m} y^{(i)}\log(h_{\theta}(x^{(i)})) + (1 - y^{(i)})\log(1 - h_{\theta}(x^{(i)}))] + \frac{\lambda}{2m}\sum_{j=1}^{n} \theta_j^2$$

Where:
- $J(\theta)$ is the cost function,
- $m$ is the number of training examples,
- $y^{(i)}$ is the actual label of the ith example,
- $h_{\theta}(x^{(i)})$ is the model's prediction for the ith example,
- $\theta_j$ are the model parameters,
- $n$ is the number of features,
- $\lambda$ is the regularization parameter that controls the strength of the regularization.

The key impact of this L2 penalty is that it discourages large weights by squaring them in the penalty term. This is beneficial because very large weights can lead to a model that is too sensitive to the input data and therefore overfits, capturing noise instead of underlying patterns. By encouraging smaller, more diffuse weight values, L2 regularization helps in reducing the model's variance without substantially increasing its bias, leading to better generalization on unseen data.

Let's examine why the other options are incorrect:
1. Incorrect. L2 regularization does not change the nature of the logistic regression model into linear regression; it only modifies the learning process by penalizing large weights.
2. Incorrect. L2 regularization does not inherently make the model learn polynomial features; it impacts the scale and distribution of the weight values.
3. Incorrect. L3 regularization encourages weights to shrink toward zero but does not necessarily make them exactly zero. L1 regularization (Lasso), not L2, is known for pushing weights to exactly zero, which can indeed aid in feature selection.
5. Incorrect. The sigmoid function, which is the activation function in logistic regression, remains unchanged by L2 regularization. The regularization affects the weight optimization process, not the shape of the activation function.