from common.r3 import R3
from math import sqrt


class TestR3:

    def test_length(self):
        a = R3(0.0, 0.0, 0.0)
        b = R3(1.0, 1.0, 1.0)
        assert a.length(b) == sqrt(3)

    def test_center_is_in_circle1(self):
        a = R3(0.0, 0.0, 0.0)
        b = R3(1.0, 1.0, 1.0)
        assert a.center_is_in_circle(b, 1)

    def test_center_is_in_circle2(self):
        a = R3(0.0, 0.0, 0.0)
        b = R3(10.0, 10.0, 10.0)
        assert not(a.center_is_in_circle(b, 1))
