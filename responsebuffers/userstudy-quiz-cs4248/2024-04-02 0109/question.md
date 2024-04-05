Given a dataset with three classes (Class 1, Class 2, and Class 3) to be predicted based on two features ($x_1$ and $x_2$), a data scientist decides to use multinomial logistic regression. The dataset is linearly separable for Class 1 but not for Class 2 and Class 3. To enhance the model's performance and avoid overfitting, the scientist contemplates incorporating regularization. During the training process, the cross-entropy loss is used as the loss function, and gradient descent is applied for optimization.

Which of the following statements is INCORRECT regarding the improvement of the model's performance in this scenario?

1. Incorporating L2 regularization would help prevent overfitting by penalizing large weights in the model.
2. Using a multinomial logistic regression model with a strong L1 regularization could lead to sparse representations, potentially reducing the model’s ability to distinguish between Class 2 and Class 3.
3. Lowering the learning rate in the gradient descent optimization could prevent oscillations and ensure convergence to the global minimum of the loss function.
4. Applying gradient descent with a very small step size could accelerate convergence by making the optimization process more responsive to changes in the loss landscape.
5. Optimizing the model with both L1 and L2 regularization, known as Elastic Net regularization, could offer a balanced approach to limiting overfitting while maintaining model complexity.