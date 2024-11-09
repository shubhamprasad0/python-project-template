from my_project.adder import Adder


class TestAdder:
    def test_add_two(self):
        adder_obj = Adder()
        num1 = 1
        num2 = 3
        result = adder_obj.add_two(num1, num2)
        assert result == 4
