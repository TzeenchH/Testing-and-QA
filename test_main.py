import _pytest
from allpairspy import AllPairs

import main
import pytest


def test_all_is_ok():
    result = main.calc_bonus(100000, 10, 4.1)
    assert 20000 == result


def test_incorrect_value_value_error():
    with pytest.raises(ValueError):
        main.calc_bonus(70000, 10, 4)


def test_incorrect_type_type_error():
    with pytest.raises(TypeError):
        main.calc_bonus("adad", 10, 5)


null_exception_test_preset = [
    dict(salary=None, level=10, perf_level=4),
    dict(salary=75000, level=None, perf_level=4),
    dict(salary=75000, level=10, perf_level=None)
]


@pytest.mark.parametrize("preset", null_exception_test_preset)
def test_null_argument_null_argument_exception(preset):
    with pytest.raises(main.NullAgrumentException):
        main.calc_bonus(salary=preset.get("salary"),
                        level=preset.get("level"),
                        perf_level=preset.get("perf_level"))


"""Граничные значения зарплаты"""
preset_salary_borders = [69900, 70000, 750000, 751000]
"""Граничные значения уровня"""
preset_level_borders = [6, 7, 17, 18]
"""Граничные значения оценки производительности"""
preset_perf_level_borders = [0.9, 1, 5, 5.1]
"""Минимальное возможное значение бонуса"""
min_result = 0
"""Максимальное возможное значение бонуса"""
max_result = 300000


# @pytest.mark.parametrize(["salary", "level", "perf_level"], [values for values in
#                                                              AllPairs([preset_salary_borders,
#                                                                        preset_level_borders,
#                                                                        preset_perf_level_borders])])
# def test_calc_bonus_borders(salary, level, perf_level):
#     try:
#         with pytest.raises(ValueError) as exc:
#             result = main.calc_bonus(salary=salary, level=level, perf_level=perf_level)
#         assert str(exc.value) in ["Зарплата не соответствует диапазону",
#                                   "Недопустимый уровень инженера",
#                                   "Неверное значение Performance Review"]
#     except _pytest.outcomes.Failed:
#         assert min_result < result < max_result
