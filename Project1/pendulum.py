"""
Part 2
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate as scint


class Pendulum:
    def __init__(self, L=1, M=1, g=9.81):
        self.L = L
        self.M = M
        self.g = g

    def __call__(self, t, y):
        """
        returns RHS of the 2 coupled ODE
        specified in task 2
        """
        self.y_1, self.y_2 = y
        return (self.y_2, -self.g / self.L * np.sin(self.y_1))

    def solve(self, u0, T, dt, angles="rad"):
        """
        Solves the exponential decay differential equation
        with the scipy.integrate.solve_ivp function.

        Input:
            - U0 initial conditions as (theta_0, omega_0)
            - T last timestep
            - dt length of each step
                    - angles either degrees or radians, will convert u0 to degrees if specified
                    - raises exception should angles be wrongly defined ie not rad or deg
        Saves solutions into arrays _theta, _omega
        which can be accessed through @property functions.
        """
        if angles == "rad":
            sol = scint.solve_ivp(
                self.__call__, (0, T), np.array(u0), t_eval=np.arange(0, T, dt)
            )
            self._t = sol.t
            self._theta, self._omega = sol.y
        elif angles == "deg":
            t, o = np.array(u0)
            theta = 180 / np.pi * t
            omega = 180 / np.pi * o
            sol = scint.solve_ivp(
                self.__call__,
                (0, T),
                np.array((theta, omega)),
                t_eval=np.arange(0, T, dt),
            )
            self._t = sol.t
            self._theta, self._omega = sol.y
        else:
            raise ValueError(
                "Angles must be set to either radians: rad or degrees: deg"
            )

    @property
    def omega(self):
        return self._omega

    @property
    def t(self):
        return self._t

    @property
    def theta(self):
        return self._theta

    @property
    def x(self):
        return self.L * np.sin(self.theta)

    @property
    def y(self):
        return -self.L * np.cos(self.theta)

    @property
    def potential(self):
        return self.M * self.g * (self.y + self.L)

    @property
    def vx(self):
        return np.gradient(self.x, self.t)

    @property
    def vy(self):
        return np.gradient(self.y, self.t)

    @property
    def kinetic(self):
        return 0.5 * self.M * (self.vx ** 2 + self.vy ** 2)


class DampenedPendulum(Pendulum):
    """
    Class inherits most methods from
    Pendulum.
    DampenedPendulum will take into account
    decaying energy throughtout motion.
    """

    def __init__(self, B=0.3, L=1, M=1, g=9.81):
        super().__init__(L, M, g)
        self.B = B

    def __call__(self, t, y):
        """
        Inherits from Pendulum.
        Returns RHS from ODE specified in
        task 2g aswell as the ODEs from task 2.
        """
        super().__call__(t, y)
        return (
            self.y_2,
            -self.g / self.L * np.sin(self.y_1) - self.B / self.M * self.y_2,
        )


if __name__ == "__main__":
    inst = Pendulum()
    inst.solve((0, np.pi / 3), 10, 0.1)
    x = inst.x
    y = inst.y
    vx = inst.vx
    vy = inst.vy
    kinetic = inst.kinetic
    potential = inst.potential
    t = inst.t
    theta = inst.theta

    inst2 = DampenedPendulum()
    inst2.solve((0, np.pi / 3), 10, 0.1)
    x2 = inst2.x
    y2 = inst2.y
    vx2 = inst2.vx
    vy2 = inst2.vy
    kinetic2 = inst2.kinetic
    potential2 = inst2.potential
    t2 = inst2.t
    theta2 = inst2.theta

    plt.subplot(2, 2, 3)
    plt.plot(t, theta)
    plt.title("Motion of pendulum")
    plt.legend([r"Motion $\theta(t)$"], loc="upper right")
    plt.xlabel("Time [s]")
    plt.ylabel("Position [m]")
    plt.subplot(2, 2, 2)
    plt.plot(t, kinetic, "r-", t, potential, "b-", t, kinetic + potential, "k-")
    plt.title("Kinetic, Potential and Total energy")
    plt.legend(["K", "P", "E"], loc="upper right")
    plt.xlabel("Time [s]")
    plt.ylabel("Energy [J]")
    plt.subplot(2, 2, 1)
    plt.plot(t2, kinetic2 + potential2, "k-")
    plt.title("Decaying energy for dampened pendulum")
    plt.legend(["E"])
    plt.xlabel("Time [t]")
    plt.ylabel("Energy [J]")
    plt.tight_layout()
    plt.show()
