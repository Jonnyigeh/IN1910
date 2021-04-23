"""
Part 1
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate as scint


class ExponentialDecay:
    def __init__(self, decay_constant):
        self.a = decay_constant

    def __call__(self, t, u):
        self.t = t
        self.u = u
        return -self.a * self.u

    def solve(self, u0, T, dt):
        """
        Solves the exponential decay differential equation
        with the scipy.integrate.solve_ivp function.

        Input:
            - U0 initial conditions
            - T last timestep
            - dt length of each step
        Output:
            - sol.t = timesteps
            - sol.y = solution for each timestep
        """
        sol = scint.solve_ivp(self.__call__, (0, T), [u0], t_eval=np.arange(0, T, dt))
        return sol.t, sol.y[0]


if __name__ == "__main__":
    a = 1
    u0 = 5
    T = 10
    dt = 0.1

    decay_model = ExponentialDecay(a)
    t, u = decay_model.solve(u0, T, dt)

    plt.plot(t, u)
    plt.show()
