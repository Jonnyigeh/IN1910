"""
Part 3
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate as scint


class DoublePendulum:
    def __init__(self, L1=1, L2=1, M1=1, M2=1, g=9.81):
        self.L1 = L1
        self.L2 = L2
        self.M1 = M1
        self.M2 = M2
        self.g = g

    def delta(self, theta1, theta2):
        """
        Returns delta theta
        """
        return theta2 - theta1

    def domega1_dt(self, M1, M2, L1, L2, theta1, theta2, omega1, omega2):
        """
        Returns the derivative of omega_1 as specified
        in task 3.
        """
        theta = self.delta(theta1, theta2)
        M1 = self.M1
        M2 = self.M2
        L1 = self.L1
        L2 = self.L2
        g = self.g
        return (
            M2 * L1 * omega1 ** 2 * np.sin(theta) * np.cos(theta)
            + M2 * g * np.sin(theta2) * np.cos(theta)
            + M2 * L2 * omega2 ** 2 * np.sin(theta)
            - (M1 + M2) * g * np.sin(theta1)
        ) / ((M1 + M2) * L1 - M2 * L1 * np.cos(theta) ** 2)

    def domega2_dt(self, M1, M2, L1, L2, theta1, theta2, omega1, omega2):
        """
        Returns the derivative of omega_2 as specified
        in task 3.
        """
        theta = self.delta(theta1, theta2)
        M1 = self.M1
        M2 = self.M2
        L1 = self.L1
        L2 = self.L2
        g = self.g
        return (
            -M2 * L2 * omega2 ** 2 * np.sin(theta) * np.cos(theta)
            + (M1 + M2) * g * np.sin(theta1) * np.cos(theta)
            - (M1 + M2) * L1 * omega1 ** 2 * np.sin(theta)
            - (M1 + M2) * g * np.sin(theta2)
        ) / ((M1 + M2) * L2 - M2 * L2 * np.cos(theta) ** 2)

    def __call__(self, t, u):
        """
        Returns the RHS of the 4 coupled
        differential equations in task 3.
        """
        self.thet1, self.omeg1, self.thet2, self.omeg2 = u
        self.domega1 = self.domega1_dt(
            self.M1,
            self.M2,
            self.L1,
            self.L2,
            self.thet1,
            self.thet2,
            self.omeg1,
            self.omeg2,
        )
        self.domega2 = self.domega2_dt(
            self.M1,
            self.M2,
            self.L1,
            self.L2,
            self.thet1,
            self.thet2,
            self.omeg1,
            self.omeg2,
        )
        return (self.omeg1, self.domega1, self.omeg2, self.domega2)

    def solve(self, u0, T, dt, angles="rad"):
        """
        Solves the exponential decay differential equation
        with the scipy.integrate.solve_ivp function.

        Input:
            - U0 initial conditions as (theta1_0, omega1_0, theta2_0, omega2_0)
            - T last timestep
            - dt length of each step
                    - angles either degrees or radians, will convert u0 to degrees if specified
                    - raises exception should angles be definer wrongly ie not rad or deg

        Saves solutions to arrays _theta1, _omega1, _theta2, _omega2
        which can be accessed through @property functions.
        """
        if angles == "rad":
            sol = scint.solve_ivp(
                self.__call__,
                (0, T),
                np.array(u0),
                t_eval=np.arange(0, T, dt),
                method="Radau",
            )
            self._t = sol.t
            self._theta1, self._omega1, self._theta2, self._omega2 = sol.y
        elif angles == "deg":
            t1, o1, t2, o2 = np.array(u0)
            theta1 = 180 / np.pi * t1
            theta2 = 180 / np.pi * t2
            omega1 = 180 / np.pi * o1
            omega2 = 180 / np.pi * o2
            sol = scint.solve_ivp(
                self.__call__,
                (0, T),
                np.array((theta1, omega1, theta2, omega2)),
                t_eval=np.arange(0, T, dt),
                method="Radau",
            )
            self._t = sol.t
            self._theta1, self._omega1, self._theta2, self._omega2 = sol.y
        else:
            raise ValueError(
                "Angles must be set to either radians: rad or degrees: deg"
            )

    @property
    def t(self):
        return self._t

    @property
    def theta1(self):
        return self._theta1

    @property
    def theta2(self):
        return self._theta2

    @property
    def x1(self):
        return self.L1 * np.sin(self._theta1)

    @property
    def y1(self):
        return -self.L1 * np.cos(self._theta1)

    @property
    def x2(self):
        return self.x1 + self.L2 * np.sin(self._theta2)

    @property
    def y2(self):
        return self.y1 - self.L2 * np.cos(self._theta2)

    @property
    def potential(self):
        return self.M1 * self.g * (self.y1 + self.L1) + self.M2 * self.g * (
            self.y2 + self.L1 + self.L2
        )

    @property
    def vx1(self):
        return np.gradient(self.x1, self._t)

    @property
    def vy1(self):
        return np.gradient(self.y1, self._t)

    @property
    def vx2(self):
        return np.gradient(self.x2, self._t)

    @property
    def vy2(self):
        return np.gradient(self.y2, self._t)

    @property
    def kinetic(self):
        return 0.5 * self.M1 * (self.vx1 ** 2 + self.vy1 ** 2) + 0.5 * self.M2 * (
            self.vx2 ** 2 + self.vy2 ** 2
        )


if __name__ == "__main__":
    T = 10
    dt = 0.01
    inst = DoublePendulum()
    inst.solve(((np.pi / 6, 0, np.pi / 3, 0)), T, dt)
    t = inst.t
    vx1 = inst.vx1
    vy1 = inst.vy1
    vx2 = inst.vx2
    vy2 = inst.vy2
    kinetic = inst.kinetic
    potential = inst.potential
    plt.plot(t, kinetic, "r-", t, potential, "b-", t, kinetic + potential, "k-")
    plt.title("Kinetic, Potential and Total energy")
    plt.legend(["K", "P", "E"], loc="upper right")
    plt.xlabel("Time [s]")
    plt.ylabel("Energy [J]")
    plt.show()
