import random
import threading
from collections import defaultdict

fish_type = (None, 'плотва', 'окунь', 'лещ', 'щука',)


class Fisher(threading.Thread):
    def __init__(self, name, worms, fish_tank, lock, *args, **kwargs):
        super(Fisher, self).__init__(*args, **kwargs)
        self.name = name
        self.worms = worms
        self.caught = 0
        self.fish_tank = fish_tank
        self.fish_tank_lock = lock

    def run(self) -> None:
        for worm in range(self.worms):
            fish = random.choice(fish_type)
            if fish is not None:
                # self.fish_tank[fish] += 1
                with self.fish_tank_lock:
                    self.fish_tank[fish] += 1
                self.caught += 1
                # print(f'{self.name} поймал {fish}')


global_fish_tank = defaultdict(int)

humans = ['Бывалый', 'Трус', 'Балбес', 'Жмот', 'Старик', 'Кузьмич', 'Генерал', 'Емеля', 'Путин', 'Медведев', ]
lock = threading.Lock()
fishers = [Fisher(name=name, worms=1000000, fish_tank=global_fish_tank, lock=lock) for name in humans]

for fisher in fishers:
    fisher.start()

for fisher in fishers:
    fisher.join()

total_fish_from_fishers = sum(fisher.caught for fisher in fishers)
total_fish_in_tank = sum(global_fish_tank.values())

print(total_fish_from_fishers, total_fish_in_tank, total_fish_from_fishers - total_fish_in_tank)
