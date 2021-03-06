# coding=utf-8

import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    plt.figure()
    plt.axis([-6, 6, 0, 1])
    plt.grid(True)
    X = np.arange(-6, 6, 0.1)
    y = 1/(1+np.e**(-X))
    plt.plot(X, y, 'b-')
    plt.show()