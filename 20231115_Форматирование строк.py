# Переменные: количество участников первой команды (team1_num).
team1_name = 'Мастера кода'
team2_name = 'Волшебники Данных'
# Переменные: количество участников в обеих командах (team1_num, team2_num).
team1_num = 5
team2_num = 6
# Переменные: количество задач решённых командой 2 (score_2).
# Переменные: количество решённых задач по командам: score_1, score_2
score_1 = 40
score_2 = 42
# Переменные: время за которое команда 2 решила задачи (team1_time).
team1_time = 18015.2
team2_time = 2153.31451
# Переменные: исход соревнования (challenge_result).
def result(score_1, score_2, team1_time, team2_time):
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        return 'Победа команды Мастера кода!'
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        return 'Победа команды Волшебники Данных!'
    else:
        return 'Ничья!'
challenge_result = result(score_1, score_2, team1_time, team2_time)
# Переменные: количество задач (tasks_total) и среднее время решения (time_avg).
tasks_total = score_1 + score_2
# time_avg = 350.4
time_avg = (team1_time + team2_time) / (score_1 + score_2)

    # Использование %:
# Пример итоговой строки: "В команде Мастера кода участников: 5 ! "
print('В команде %s участников: %s !' % (team1_name, team1_num))
# Пример итоговой строки: "Итого сегодня в командах участников: 5 и 6 !"
print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))

    # Использование format():
# Пример итоговой строки: "Команда Волшебники данных решила задач: 42 !"
print('Команда {0} решила задач: {1} !'.format(team2_name, score_2))
# Пример итоговой строки: " Волшебники данных решили задачи за 18015.2 с !"
print('{0} решили задачи за {1} с !'.format(team2_name, team1_time))

    # Использование f-строк:
# Пример итоговой строки: "Команды решили 40 и 42 задач.”
print(f'Команды решили {score_1} и {score_2} задач.')
# Пример итоговой строки: "Результат битвы: победа команды Мастера кода!"
print(f'Результат битвы: {challenge_result}')
# Пример итоговой строки: "Сегодня было решено 82 задач, в среднем по 350.4 секунды на задачу!."
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.')


# Комментарии к заданию:
# В русском языке окончания слов меняются (1 участник, 2 участника), пока что давайте не обращать на это внимания.
# Переменные challenge_result, tasks_total, time_avg можно задать вручную или рассчитать. Например, для challenge_result:
# if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
# result = ‘Победа команды Мастера кода!’
# elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
# result = ‘Победа команды Волшебники Данных!’ else:
# result = ‘Ничья!’

# Пример входных данных
# team1_num = 6 team2_num = 6
# score1 = 40
# score2 = 42
# team1_time = 1552.512 team2_time = 2153.31451 tasks_total = 82
# time_avg = 45.2
# challenge_result = 'Победа команды Волшебники данных!'
