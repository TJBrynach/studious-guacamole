import numpy as np

def predict(X, w):
    return np.matmul(X, w)

def loss(X, Y, w):
    return np.average((predict(X, w) -Y) ** 2)

def gradient(X, Y, w):
    return 2 * np.matmul(X.T, (predict(X, w) -Y)) / X.shape[0]

def train(X, Y, iterations, lr):
    w = np.zeros((X.shape[1],1))
    for i in range(iterations):
        print("Iterations %4d => Loss: %.20f" % (i, loss(X, Y, w)))
        w -= gradient(X, Y, w) * lr
    return w

life_exp_path = '/Users/thomasshorney/studious-guacamole/code/life-expectancy-without-country-names.txt'
x1, x2, x3, y = np.loadtxt(life_exp_path,skiprows=1, unpack=True)
X = np.column_stack((np.ones(x1.size), x1, x2, x3)) # turning all the unpacked data into a matrix of X and adding our bias
Y = y.reshape(-1,1)
w = train(X, Y, iterations=5_000_000, lr=0.0001)


print("\nWeights: %s" % w.T)
print("\nA few predictions:")
for i in range(5):
    print("X[%d] -> %.4f (label: %d)" % (i, predict(X[i], w), Y[i]))



"""Weights: [[37.03603424 -0.05407308  0.23120919  0.38537   ]]

A few predictions:
X[0] -> 75.5160 (label: 76)
X[1] -> 75.2524 (label: 74)
X[2] -> 77.4308 (label: 82)
X[3] -> 77.2738 (label: 81)
X[4] -> 70.1363 (label: 71)

Which is not good enough, because even if we round them, only 1 of the 5 was correct
"""