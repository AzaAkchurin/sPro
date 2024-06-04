def calculate_bonus(yearly_salary, work_days, took_day_off):
    if work_days > 3 * 365:
        bonus_percentage = 0.30
    elif 1.5 * 365 < work_days <= 3 * 365:
        bonus_percentage = 0.25
    elif 90 < work_days <= 1.5 * 365:
        bonus_percentage = 0.15
    else:
        bonus_percentage = 0.0

    if not took_day_off:
        bonus_percentage += 0.03

    bonus = yearly_salary * bonus_percentage
    return round(bonus)


def test_calculate_bonus():
    assert calculate_bonus(100000, 10 * 365, True) == 30000.0
    assert calculate_bonus(100000, 2 * 365, False) == 28000.0
    assert calculate_bonus(100000, 365, True) == 15000.0
    assert calculate_bonus(100000, 30, False) == 3000.0
    assert calculate_bonus(100000, 365, False) == 18000.0
    assert calculate_bonus(100000, 4 * 365, False) == 33000.0
    assert calculate_bonus(100000, 2 * 365, True) == 25000.0


test_calculate_bonus()
print("Все тесты пройдены успешно")
