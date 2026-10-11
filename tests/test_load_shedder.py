import pytest
from load_shedder import decide
from signal_filter import MovingAverageFilter


def test_normal_load_stays_nominal():
    assert decide(70, True, 0) is True

def test_sheds_when_surge_is_sustained():
    assert decide(110, True, 2) is False

def test_does_not_shed_on_single_spike():
    assert decide(110, True, 1) is True

def test_stays_shed_while_predicted_load_too_high():
    assert decide(60, False, 0) is False      # 60 + 40 = 100, not < 80

def test_reengages_when_predicted_load_is_safe():
    assert decide(30, False, 0) is True       # 30 + 40 = 70 < 80

def test_boundary_exactly_at_recover_limit_stays_shed():
    assert decide(40, False, 0) is False      # 40 + 40 = 80, not < 80

def test_filter_averages_last_three():
    f = MovingAverageFilter(window_size=3)
    for x in (10, 20, 30, 40):
        result = f.filter_noise(x)
    assert result == pytest.approx(30)        # (20 + 30 + 40) / 3