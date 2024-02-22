import random
import threading
from collections import defaultdict
from multiprocessing import Process, Pipe

fish_type = (None, 'плотва', 'окунь', 'лещ', 'щука',)


class Fisher(Process):
    def __init__(self, name, worms, conn, *args, **kwargs):
        super(Fisher, self).__init__(*args, **kwargs)
        self.name = name
        self.worms = worms
        self.catched = 0
        self.conn = conn

    def run(self) -> None:
        catch = defaultdict(int)
        for worm in range(self.worms):
            print(f'забросил')
            _ = 3 ** (random.randint(50, 70) * 10000)
            fish = random.choice(fish_type)
            if fish is not None:
                print(f'{self.name}: ага у меня {fish}')
                catch[fish] += 1
                self.catched += 1

        print(f'{self.name} поймал {catch}')
        self.conn.send([self.name, self.catched])
        self.conn.close()


if __name__ == '__main__':
    # global_fish_tank = defaultdict(int)

    humans = ['Бывалый', 'Трус', 'Балбес', 'Жмот', 'Старик', 'Кузьмич', 'Генерал', 'Емеля', 'Путин', 'Медведев', ]
    fishers, pipes = [], []
    for name in humans:
        parent_conn, child_conn = Pipe()
        fisher = Fisher(name=name, worms=10, conn=child_conn)
        fishers.append(fisher)
        pipes.append(parent_conn)
    for fisher in fishers:
        fisher.start()
    total_fish = 0
    for conn in pipes:
        name, fish_count = conn.recv()
        total_fish += fish_count
    for fisher in fishers:
        fisher.join()
    print(f'итого поймали: {total_fish}')
