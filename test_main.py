import main
import pytest


def test_all_is_ok():
    result = main.calc_bonus(100000, 10, 4.1)
    assert 20000 == result


@pytest.mark.parametrize(
    "salary, level, perf_level, expected_msg",
    [
        (69999, 10, 4, "Зарплата не соответствует диапазону"),
        (750001, 10, 4, "Зарплата не соответствует диапазону"),
        (85000, 6, 4, "Недопустимый уровень инженера"),
        (85000, 16, 4, "Недопустимый уровень инженера"),
        (85000, 10, 0, "Неверное значение Performance Review"),
        (85000, 10, 6, "Неверное значение Performance Review"),
    ]
)
def test_incorrect_value_value_error(salary, level, perf_level, expected_msg):
    with pytest.raises(ValueError, match=expected_msg):
        main.calc_bonus(salary, level, perf_level)


def test_incorrect_type_type_error():
    with pytest.raises(TypeError, match="Введены данные некорректного формата"):
        main.calc_bonus("adad", 10, 5)


@pytest.mark.parametrize(
    "salary, level, perf_level",
    [
        (None, 10, 4),
        (75000, None, 4),
        (75000, 10, None),
    ]
)
def test_null_argument_null_argument_exception(salary, level, perf_level):
    with pytest.raises(main.NullAgrumentException, match="Один из входных параметров не определён"):
        main.calc_bonus(salary=salary, level=level, perf_level=perf_level)


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
