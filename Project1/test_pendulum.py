"""
Test for Part 2
"""
import numpy as np
import pytest
from pendulum import Pendulum


def test_pendulum_derivative():
    """
    Checks that our __call__ method
    returns the correct derivative for some
    arbitrary numbers.
    """
    expected = (0.15, -1.8166666667)
    L = 2.7
    omega = 0.15
    theta = np.pi / 6
    inst = Pendulum(L)
    computed = inst(1, (theta, omega))
    tol = 1e-10
    assert abs(expected[1] - computed[1]) < tol


def test_pendulum_equillibruim():
    """
    Checks that a pendulum that starts
    at rest, will stay at rest.
    """
    inst = Pendulum()
    theta = 0
    omega = 0
    computed = inst(1, (theta, omega))
    tol = 1e-10
    assert computed == (0, 0)


def test_pendulum_solve_exceptions():
    """
    Checks that our program returns errors should
    we try to access solutions before they have been
    computed.
    """
    inst = Pendulum()
    with pytest.raises(AttributeError):
        inst.t
    with pytest.raises(AttributeError):
        inst.theta
    with pytest.raises(AttributeError):
        inst.omega


def test_pendulum_solve_equillibrium():
    """
    Checks that the solution using scipy.integrate.solve_ivp
    will remain at rest, given initial conditions at rest.
    """
    omega = 0
    theta = 0
    T = 10
    dt = 0.1
    inst = Pendulum()
    expected_t = np.arange(0, T, dt)
    expected_theta = np.zeros_like(expected_t)
    expected_omega = np.zeros_like(expected_t)
    inst.solve((theta, omega), T, dt)
    assert all(inst.t == expected_t)
    assert all(inst.theta == expected_theta)
    assert all(inst.omega == expected_omega)


def test_pendulum_radius():
    """
    Checks that the radius for our pendulum-
    motion remains fairly constant
    """
    inst = Pendulum()
    inst.solve((0, np.pi / 3), 10, 0.1)
    x = inst.x
    y = inst.y
    L = inst.L
    tol = 1e-10
    assert all(abs((x ** 2 + y ** 2) - L ** 2) < tol)


if __name__ == "__main__":
    pass
