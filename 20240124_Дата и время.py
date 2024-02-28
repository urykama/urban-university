import datetime


class SuperDate(datetime.datetime):

    def get_season(self) -> str:
        season = ["Winter", "Spring", "Summer", "Autumn", "Winter"]
        return season[a.month // 3]

        # # вариант из интернета (через match-case)
        # match a.month:
        #     case 1 | 2 | 12:
        #         return "Winter"
        #     case 3 | 4 | 5:
        #         return "Spring"
        #     case 6 | 7 | 8:
        #         return "Summer"
        #     case 9 | 10 | 11:
        #         return "Autumn"
        #     case _:
        #         return "Error"

    def get_time_of_day(self) -> str:
        time_of_day = ['Night', 'Morning', 'Day', 'Evening', ]
        return time_of_day[a.hour // 6]
        # проверка на Ошибку, что число вне диапазона можно не делать,
        # т.к. класс сам проверяет правильность ввода даты

        # # вариант со словарем
        # time_of_day = {'Night': range(6),
        #                'Morning': range(6, 12),
        #                'Day': range(12, 18),
        #                'Evening': range(18, 24), }
        # for key in time_of_day.keys():
        #     if a.hour in time_of_day[key]:
        #         return key
        # return "Error"

        # # вариант из интернета (через match-case)
        # match a.hour:
        #     case 0 | 1 | 2 | 3 | 4 | 5:
        #         return "Night"
        #     case 6 | 7 | 8 | 9 | 10 | 11:
        #         return "Morning"
        #     case 12 | 13 | 14 | 15 | 16 | 17:
        #         return "Day"
        #     case 18 | 19 | 20 | 21 | 22 | 23:
        #         return "Evening"
        #     case _:
        #         return "Error"


a = SuperDate(2024, 2, 22, 12)
print(a.get_season())
print(a.get_time_of_day())

# # проверка работы с месяцами
# for i in range(1, 13):
#     print(i)
#     a = SuperDate(2024, i, 22, 12)
#     print(a.get_season())
#     print()
