import numpy as np
import mnist as data
import gzip
import struct

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def forward(X, w):
    weighted_sum = np.matmul(X , w)
    return sigmoid(weighted_sum)

def classify(X, w):
    y_hat = forward(X, w)
    labels = np.argmax(y_hat, axis = 1)
    return labels.reshape(-1,1)

def loss(X, Y, w):
    y_hat = forward(X, w)
    first_term = Y * np.log(1 - y_hat)
    second_term =  (1 - Y) * np.log(1 - y_hat)
    return - np.average(first_term + second_term) / X.shape[0]

def gradient(X, Y, w):
    return np.matmul(X.T, (forward(X, w) - Y)) / X.shape[0]

def report(iteration, X_train, Y_train, X_test, Y_test, w):
    matches = np.count_nonzero(classify(X_test, w) == Y_test)
    n_test_examples = Y_test.shape[0]
    matches = matches * 100.0 / n_test_examples
    training_loss = loss(X_train, Y_train, w)
    print("%d - Loss: %.20f, %.2f%%" % (iteration, training_loss, matches))


def train(X_train, Y_train, X_test, Y_test, iterations, lr):
    w = np.zeros((X_train.shape[1], Y_train.shape[1]))
    for i in range(iterations):
        report(i, X_train, Y_train, X_test, Y_test, w)
        w -= gradient(X_train, Y_train, w) * lr
    report(iterations, X_train, Y_train, X_test, Y_test, w)
    return w

def load_images(filename):
    with gzip.open(filename, 'rb') as f:

        _ignored, n_images, columns, rows = struct.unpack('>IIII', f.read(16))

        all_pixels = np.frombuffer(f.read(), dtype=np.uint8)

        return all_pixels.reshape(n_images, columns * rows)

def prepend_bias(X):
    return np.insert(X, 0, 1, axis=1)

def load_labels(filename):
    with gzip.open(filename, 'rb') as f:
        f.read(8)
        all_labels = f.read()
        return np.frombuffer(all_labels, dtype=np.uint8).reshape(-1,1)

def one_hot_encode(Y):
    n_labels = Y.shape[0]
    n_classes = 10
    encoded_Y = np.zeros((n_labels, n_classes))
    for i in range(n_labels):
        label = Y[i]
        encoded_Y[i][label] = 1
    return encoded_Y

Y_train = one_hot_encode(load_labels("/Users/thomasshorney/code/data/mnist/train-labels-idx1-ubyte.gz"))
Y_test = one_hot_encode(load_labels("/Users/thomasshorney/code/data/mnist/t10k-labels-idx1-ubyte.gz"))
     
X_train = prepend_bias(load_images("/Users/thomasshorney/code/data/mnist/train-images-idx3-ubyte.gz"))
X_test = prepend_bias(load_images("/Users/thomasshorney/code/data/mnist/t10k-images-idx3-ubyte.gz"))

w = train(X_train, Y_train, X_test, Y_test, iterations=200, lr=1e-5)
