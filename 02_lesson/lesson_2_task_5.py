num = 12


def month_to_season(num):
    if (12 == num) or 1 <= num <= 2:
        return "Зима"
    elif 3 <= num <= 5:
        return "Весна"
    elif 6 <= num <= 8:
        return "Лето"
    elif 9 <= num <= 11:
        return "Осень"


print(month_to_season(num))
