"""
Test for Part1a
"""
from exp_decay import ExponentialDecay


def test_ExponentialDecay():
    dudt = -1.28
    u = 3.2
    t = "nan"
    a = 0.4
    inst = ExponentialDecay(a)
    tol = 1e-10
    assert (dudt - inst(t, u)) < tol


if __name__ == "__main__":
    test_ExponentialDecay()
