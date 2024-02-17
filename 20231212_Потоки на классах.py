from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name: str, skill: int, color: str, *args, **kwargs):
        super(Knight, self).__init__(*args, **kwargs)
        self.name = name
        self.skill = skill
        self.color = color
        self.day = 0

    def run(self) -> None:
        print(f'{self.color}Sir {self.name}, на нас напали!')
        for i in range(100 - self.skill, 0, -self.skill):
            sleep(1)
            self.day += 1
            print(f'{self.color}Sir {self.name}, сражается {self.day} день(дня)..., осталось {i} воинов.')

        print(f'{self.color}Sir {self.name}, одержал победу спустя 5 дней!')


knight1 = Knight("Sir Lancelot", 10, '\033[31m')  # Низкий уровень умения
knight2 = Knight("Sir Galahad", 20, '\033[32m')  # Высокий уровень умения
knight1.start()
knight2.start()
knight1.join()
knight2.join()
print('\033[0m', 'Все битвы закончились!')
