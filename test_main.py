
import main
import pytest
import allpairspy


def test_all_is_ok():
    result = main.calc_bonus(100000, 10, 4)
    assert 20000 == result


def test_incorrect_value_value_error():
    with pytest.raises(ValueError):
        main.calc_bonus(70000, 10, 4)


salaries = list(range(70000, 750001, 1000))
levels = list(range(7, 18))
perf_results = list(x * 0.1 for x in range(10, 51))
parameters = [
    salaries,
    levels,
    perf_results,
]

feed_to_test = allpairspy.AllPairs(parameters)
