import decimal

"""
   Необходимо реализовать механизм расчета премии по результатам Performance Review программиста.
   Для предоставляемых данных:
   - ЗП инженера - [70 000..750 000] (только целочисленные значения или преобразование ЗП в таковое)
   - Результат квартального Performance Review [1..5]
   - Уровень инженера - [7..17]
   - Размер премии от квартальной ЗП:
       - 5% если lvl < 10;
       - 10% если 10 <= lvl < 13
       - 15% если 13 <= lvl < 15
       - 20% если lvl >= 15
   > - Модификатор премии:
   >   - 0% - если результат pref-review < 2
   >   - 25% - если 2 <= результат pref-review < 2.5
   >   - 50% - если 2.5 <= результат pref-review < 3
   >   - 100% - если 3 <= результат pref-review < 3.5
   >   - 150% - если 3.5 <= результат pref-review < 4
   >   - 200% - если результат pref-review >= 4
   """


def calc_level_modifier(level: int) -> decimal:
    if level < 10:
        level_bonus = 0.05
    elif 10 <= level < 13:
        level_bonus = 0.1
    elif 13 <= level < 15:
        level_bonus = 0.15
    else:
        level_bonus = 0.2
    return level_bonus


def calc_performance_modifier(perf_level: int):
    perf_bonus = 0
    if 2 <= perf_level < 2.5:
        perf_bonus = 0.25
    elif 2.5 <= perf_level < 3:
        perf_bonus = 0.5
    elif 3 <= perf_level < 3.5:
        perf_bonus = 1
    elif 3.5 <= perf_level < 4:
        perf_bonus = 1.5
    else:
        perf_bonus = 2
    return perf_bonus


def calc_bonus(salary: int, level: int, perf_level: decimal) -> float:
    if salary is not int or level is not int:
        raise TypeError("Введены данные некорректного формата")
    if salary < 70000 or 750000 < level:
        raise ValueError("Зарплата не соответствует диапазону")
    if level < 7 or 15 < level:
        raise ValueError("Недопустимый уровень инженера")
    if perf_level < 1 or 5 < perf_level:
        raise ValueError("Неверное значение Performance Review")
    if salary is None or level is None or perf_level is None:
        raise NullAgrumentException("Один из входных параметров не определён")
    level_modifier = calc_level_modifier(level)
    perf_modifier = calc_performance_modifier(perf_level)

    bonus = salary * level_modifier * perf_modifier
    return bonus


class NullAgrumentException(Exception):
    def __init__(self, message):
        self.message = message
