from rock_paper_scissors import Blimey


def test_two_times_two_equals_four():
    assert 2 * 2 == 4


class TestBlimey:
    def test_blimey_increases_by_9000(self):
        blimey = Blimey()
        assert blimey.increase_by_9000(1) == 9001
