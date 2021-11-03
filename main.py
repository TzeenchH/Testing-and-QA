def calc_bonus(salary: int, level: int, perf_level: float) -> float:
    if salary is not int or level is not int:
        raise TypeError("Введены данные некорректного формата")
    if salary < 70000 or 750000 < level:
        raise ValueError("Зарплата не соответствует диапазону")
    if level < 7 or 15 < level:
        raise ValueError("Недопустимый уровень инженера")
    if perf_level < 1 or 5 < perf_level:
        raise ValueError("Неверное значение Performance Review")
    level_bonus = 0
    perf_bonus = 0
    if level < 10:
        level_bonus = 0.05
    elif 10 <= level < 13:
        level_bonus = 0.1
    elif 13 <= level < 15:
        level_bonus = 0.15
    else:
        level_bonus = 0.2

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

    bonus = salary * level_bonus * perf_bonus
    return bonus
