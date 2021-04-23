"""
Test task 3
"""
import numpy as np
import pytest
from double_pendulum import DoublePendulum


def test_double_pendulum_equillibrium():
    """
    Checks that our double pendulum system remains
    at rest if it is initially at rest.
    At rest meaning here that all angles, and angular velocities
    are equal to zero.
    """
    omega1 = 0
    theta1 = 0
    omega2 = 0
    theta2 = 0
    T = 10
    dt = 0.1
    inst = DoublePendulum()
    expected_t = np.arange(0, T, dt)
    expected_theta = np.zeros_like(expected_t)
    expected_omega = np.zeros_like(expected_t)
    inst.solve((theta1, omega1, theta2, omega2), T, dt)
    assert all(inst.t == expected_t)
    assert all(inst.theta1 == expected_theta)
    assert all(inst.theta2 == expected_theta)
    assert all(inst._omega1 == expected_omega)
    assert all(inst._omega2 == expected_omega)


def test_double_pendulum_solve_exceptions():
    """
    Checks that our program raises the proper
    error when we try to access attributes that
    are not yet defined.
    We should not be able to find the angles
    and time array before calling the solve method.
    """
    omega1 = 0
    theta1 = 0
    omega2 = 0
    theta2 = 0
    T = 10
    dt = 0.1
    inst = DoublePendulum()
    with pytest.raises(AttributeError):
        inst.t
    with pytest.raises(AttributeError):
        inst.theta1
    with pytest.raises(AttributeError):
        inst.theta2
    with pytest.raises(AttributeError):
        inst.kinetic
    with pytest.raises(AttributeError):
        inst.potential


def test_double_pendulum_total_energy():
    """
    Checks that energy is relativly well preserved
    throughout our computations.
    We look at the discrepancy of the array of
    total energy for each timestep, and we want this to
    be smaller than our tolerance.
    """
    omega1 = 1
    theta1 = np.pi / 6
    omega2 = 0
    theta2 = np.pi / 3
    T = 10
    dt = 0.01
    inst = DoublePendulum()
    inst.solve((theta1, omega1, theta2, omega2), T, dt)
    kinetic_energy = inst.kinetic
    potential_energy = inst.potential
    total = kinetic_energy + potential_energy
    tol = 0.3
    assert max(total) - min(total) < tol


if __name__ == "__main__":
    pass
