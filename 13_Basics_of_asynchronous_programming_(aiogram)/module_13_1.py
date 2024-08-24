import asyncio


async def start_strongman(name: str, power: int):
    print(f'\033[32mСилач {name} начал соревнования.')
    [(await asyncio.sleep(2.4 / power), print(f'\033[3{power}mСилач {name} поднял {ball} шар.')) for ball in range(1, 6)]
    print(f'\033[32mСилач {name} закончил соревнования.')


async def start_tournament():
    [await task for task in [asyncio.create_task(start_strongman(*strongman))
                             for strongman in (('Pasha', 3), ('Denis', 4), ('Apollon', 5))]]


asyncio.run(start_tournament())
