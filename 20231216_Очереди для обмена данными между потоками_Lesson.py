import queue
import random
import threading
import time
from collections import defaultdict

fish_type = (None, 'плотва', 'окунь', 'лещ', 'щука',)


class Fisher(threading.Thread):
    def __init__(self, name, worms, caught, *args, **kwargs):
        super(Fisher, self).__init__(*args, **kwargs)
        # super().__init__(*args, **kwargs)
        self.name = name
        self.worms = worms
        self.caught = caught

    def run(self) -> None:
        for worm in range(self.worms):
            print(f'{self.name}, {worm}: забросили ждем...', flush=True)
            time.sleep(random.randint(0, 2) / 100)
            fish = random.choice(fish_type)
            if fish is None:
                print(f'{self.name}, {worm}: сожрали червяка!', flush=True)
            else:
                print(f'{self.name}, {worm}: поймал {fish} и хочет положить его в садок', flush=True)
                if self.caught.full():
                    print(f'\033[31m{self.name}, {worm}: приемщик полон!!!\033[0m', flush=True)
                # self.fish_tank[fish] += 1
                # with self.fish_tank_lock:
                #     self.fish_tank[fish] += 1
                self.caught.put(fish)
                print(f'{self.name}, {worm}: отдал {fish} приемщику', flush=True)


class Boat(threading.Thread):
    def __init__(self, worms_per_fisher=10, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fishers = []
        self.worms_per_fisher = worms_per_fisher
        self.caught = queue.Queue(maxsize=2)
        self.fish_tank = defaultdict(int)

    def add_fisher(self, name):
        fisher = Fisher(name=name, worms=self.worms_per_fisher, caught=self.caught)
        self.fishers.append(fisher)
        # print(fisher)

    def run(self) -> None:
        print('The boat went out to sea... (лодка вышла в море)')
        for fisher in self.fishers:
            print(fisher)
            fisher.start()
        while True:
            try:
                fish = self.caught.get(timeout=1)
                print(f'\033[32mПриемщик принял {fish} и положил в садок\033[0m', flush=True)
                self.fish_tank[fish] += 1
            except queue.Empty:
                print(f'У приемщика нет рыбы в течении 1 секунды', flush=True)
                if not any(fisher.is_alive() for fisher in self.fishers):
                    break
        for fisher in self.fishers:
            fisher.join()
        print(f'Лодка возвращается домой с {self.fish_tank}', flush=True)


boat = Boat(worms_per_fisher=10)

humans = ['Бывалый', 'Трус', 'Балбес', 'Жмот', 'Старик', 'Кузьмич', 'Генерал', 'Емеля', 'Путин', 'Медведев', ]
for name in humans:
    boat.add_fisher(name=name)

boat.start()
boat.join()

print(boat.fish_tank, 'всего:', sum(boat.fish_tank.values()))
