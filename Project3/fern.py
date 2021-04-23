import matplotlib.pyplot as plt
import numpy as np


class AffineTransform:
    def __init__(self, a=0, b=0, c=0, d=0, e=0, f=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def __call__(self, punkt):
        """
        Utfører affintransformasjonen.
        Input: Tuppel/array/liste med (x,y) punktet
        Output: transformasjon f(x,y)
        """
        x, y = punkt
        transformation = np.matmul(
            np.array(([self.a, self.b], [self.c, self.d])), np.array(([x], [y]))
        ) + np.array(([self.e], [self.f]))
        return transformation.T

def choosefunction():
    functions = [f_1, f_2, f_3, f_4]
    p_1 = 0.01
    p_2 = 0.85
    p_3 = 0.07
    p_4 = 0.07
    p_cumulative = np.array([p_1, p_1+p_2, p_1+p_2+p_3, p_1+p_2+p_3+p_4])
    r = np.random.random()
    for j, p in enumerate(p_cumulative):
        if r < p:
            return functions[j]


if __name__ == "__main__":
    f_1 = AffineTransform(d=0.16)
    f_2 = AffineTransform(a=0.85, b=0.04, c=-0.04, d=0.85, f=1.60)
    f_3 = AffineTransform(a=0.2, b=-0.26, c=0.23, d=0.22, f=1.60)
    f_4 = AffineTransform(a=-0.15, b=0.28, c=0.26, d=0.24, f=0.44)
    N = 50000
    X0 = [0,0]
    X = np.zeros((N,2))
    X[0] = X0
    for i in range(N-1):
        f = choosefunction()
        X[i+1] = f(X[i])
    plt.scatter(*zip(*X), color="forestgreen", marker=".", s=0.2)
    plt.axis([-4,4,0,11])
    #plt.savefig("barnsley_fern.png")
    plt.show()
