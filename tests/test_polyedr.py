from shadow.polyedr import Polyedr


class TestPolyedr:

    def test_polyedr_1(self):
        assert Polyedr(f"data/test1.geom").counter() == 0

    def test_polyedr_2(self):
        assert Polyedr(f"data/test2.geom").counter() == 2

    def test_polyedr_3(self):
        assert Polyedr(f"data/test3.geom").counter() == 2

    def test_polyedr_4(self):
        assert Polyedr(f"data/test4.geom").counter() == 4

    def test_polyedr_5(self):
        assert Polyedr(f"data/test5.geom").counter() == 4

    def test_polyedr_6(self):
        assert Polyedr(f"data/test6.geom").counter() == 8

    def test_polyedr_7(self):
        assert Polyedr(f"data/test7.geom").counter() == 6
