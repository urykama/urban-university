import unittest
from main import Student


class TTTest(unittest.TestCase):
    def setUp(self) -> None:
        self.student_walk = Student('Wowa')
        self.student_run = Student('Roma')

    def tearDown(self) -> None:
        pass

    def test_1(self):
        """
        Первый тест: у одного объекта должен запускать метод walk 10 раз,
        после чего должен возвращаться результат сравнения полученных данных.
        В  случае провального теста должно выводится сообщение:
        Дистанции не равны [дистанция человека(объекта)] != 500
        """
        for _ in range(10):
            self.student_walk.walk()
        self.assertEqual(self.student_walk.distance, 50,
                         'Дистанции не равны [дистанция человека(объекта)] != 500')

    def test_2(self):
        """
        Второй тест: у одного объекта должен запускать метод run 10 раз,
        после чего должен возвращаться результат сравнения полученных данных.
        В случае провального теста должно выводится сообщение:
        Дистанции не равны [дистанция человека(объекта)] != 1000
        """
        for _ in range(10):
            self.student_run.run()
        self.assertEqual(self.student_run.distance, 100,
                         'Дистанции не равны [дистанция человека(объекта)] != 1000')

    def test_3(self):
        """
        Третий тест: 2 объекта "соревнуются", один "бежит", другой "идёт" (тот самый студент, кто не посещает вебинары).
        После чего должен возвращаться результат сравнения полученных данных.
        В  случае провального теста должно выводится сообщение:
        [бегущий человек] должен преодолеть дистанцию больше, чем [идущий человек].
        """
        for _ in range(10):
            self.student_walk.walk()
            self.student_run.run()
        self.assertTrue(self.student_walk.distance < self.student_run.distance,
                        '[бегущий человек] должен преодолеть дистанцию больше, чем [идущий человек].')


if __name__ == '__main__':
    unittest.main()
