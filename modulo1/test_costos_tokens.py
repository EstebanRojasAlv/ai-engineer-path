import pytest
from costos_tokens import calculate_cost 


def test_medium_model_cost():
    assert calculate_cost("medium", 2000, 500) == pytest.approx(0.0135)


def test_quick_model_cost():
    assert calculate_cost("quick", 2000, 500) == pytest.approx(0.001125)


def test_max_model_cost():
    assert calculate_cost("max", 2000, 500) == pytest.approx(0.0675)


def test_zero_tokens_cost_nothing():
    assert calculate_cost("medium", 0, 0) == pytest.approx(0)


def test_unknown_model_raises_error():
    with pytest.raises(ValueError):
        calculate_cost("unknown_model", 2000, 500)


def test_negative_tokens_raise_error():
    with pytest.raises(ValueError):
        calculate_cost("medium", -2000, 0)


def test_negative_output_tokens_raise_error():
    with pytest.raises(ValueError):
        calculate_cost("quick", 2000, -500)

