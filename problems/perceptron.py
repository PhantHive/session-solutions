"""
Exercise: Perceptron
Goal: Given a list of inputs and outputs, find the weights and bias of a perceptron that solves the AND problem.
Example: inputs = [[0, 0], [0, 1], [1, 0], [1, 1]], outputs = [0, 0, 0, 1]
"""


def heaviside(t):
    return 1 if t >= 0 else 0


def predict(X, weights, bias):
    return heaviside(weights[0] * X[0] + weights[1] * X[1] + bias)


def perceptron(weights, bias, epochs):
    for epoch in range(epochs):
        print(f"Epoch {epoch}")
        for i in range(len(inputs)):
            X = inputs[i]
            y = outputs[i]

            y_hat = heaviside(weights[0] * X[0] + weights[1] * X[1] + bias)
            error = y - y_hat

            # Update weights and bias
            weights[0] += error * X[0]
            weights[1] += error * X[1]
            bias += error

    return weights, bias


if __name__ == '__main__':
    inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
    outputs = [0, 0, 0, 1]
    weights = [0, 0]
    bias = 1

    weights, bias = perceptron(weights, bias, epochs=6)
    print(f"\nweights: {weights}, bias: {bias}\n")

    # predict for all inputs and print the solution
    for X in inputs:
        print(f"{X[0]} AND {X[1]} = {predict(X, weights, bias)}")
