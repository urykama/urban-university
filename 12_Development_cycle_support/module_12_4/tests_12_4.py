import unittest
import logging
from tests_12_1 import Runner

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                    encoding='utf-8', format='%(asctime)s | %(levelname)s | %(message)s')


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            runner = Runner(-1)
            print(runner.__dict__)
            [runner.walk() for _ in range(10)]
            self.assertEqual(runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            runner = Runner(1)
            [runner.run() for _ in range(10)]
            self.assertEqual(runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner1, runner2 = [Runner('') for _ in range(2)]
        [(runner1.walk(), runner2.run()) for _ in range(10)]
        self.assertNotEqual(runner1.distance, runner2.distance)
