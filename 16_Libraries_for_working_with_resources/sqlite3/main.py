"""
Цель задания:
Научиться использовать функционал sqlite3 для работы с базами данных.

Задание:
Студентов Urban'а становиться всё больше с каждым месяцем (не может не радовать), поэтому
вам было поручено создать базу данных для отслеживания их и вашего прогресса в обучении.
Т.к. вести все записи через Excel и прописывать формулы наши кураторы устали (неправда :) ),
нужно создать базу данных и автоматизировать работу с ней при помощи ООП."""
import random
import sqlite3
from pprint import pprint

# Создайте базу данных students.db

conn = sqlite3.connect("students.db")

# В базе данных должны существовать 2 таблицы: students и grades
# В таблице students должны присутствовать следующие поля: id, name, age
conn.execute("""CREATE TABLE  IF NOT EXISTS students(
                id          INTEGER     PRIMARY KEY, 
                name        STR, 
                age         INTEGER)""")
# В таблице grades должны присутствовать следующие поля: id, student_id, subject, grade
conn.execute("""CREATE TABLE IF NOT EXISTS grades(
               id           INTEGER     PRIMARY KEY, 
               student_id   INTEGER, 
               subject      STR, 
               grade        FLOAT,
               FOREIGN KEY (student_id) REFERENCES students(id))""")


# FOREIGN KEY fk_user_id  (student_id) REFERENCES students(id),
# FOREIGN KEY (student_id) REFERENCES students(id),


class University:
    """Так же нужно создать класс University со следующими атрибутами и методами:
    name - имя университета
    add_student(name, age) - метод добавления студента.
    add_grade(sudent_id, subject, grade) - метод добавления оценки.
    get_students(subject=None) - метод для возврата списка студентов в формате
    [(Ivan, 26, Python, 4.8), (Ilya, 24, PHP, 4.3)],
    где subject, если не является None(по умолчанию) и если такой предмет существует,
    выводит студентов только по этому предмету."""

    def __init__(self, name):
        self.name = name

    def add_student(self, name: str, age: int) -> None:
        conn.execute(f"INSERT INTO students (name, age) "
                     f"VALUES('{name}', '{age}')")
        conn.commit()

    def add_grade(self, sudent_id: int, subject: str, grade: float) -> None:
        conn.execute(f"INSERT INTO grades (student_id, subject, grade) "
                     f"VALUES('{sudent_id}', '{subject}', '{grade}')")
        conn.commit()

    def get_students(self, subject=None):
        cursor = conn.cursor()
        if subject is None:
            cursor.execute(
                'SELECT students.name, students.age, grades.subject, grades.grade FROM students, '
                'grades WHERE grades.student_id = students.id')
            return cursor.fetchall()
        else:
            cursor.execute(
                f'SELECT students.name, students.age, grades.subject, grades.grade FROM students, '
                f'grades WHERE grades.student_id = students.id AND grades.subject = "{subject}"')
            return cursor.fetchall()


def test_1():
    u1 = University('Urban')
    u1.add_student('Ivan', 26)  # id - 1
    u1.add_student('Ilya', 24)  # id - 2
    u1.add_grade(1, 'Python', 4.8)
    u1.add_grade(2, 'PHP', 4.3)
    print(u1.get_students())
    print(u1.get_students('Python'))
    """
    Консоль:
    [('Ivan', 26, 'Python', 4.8), ('Ilya', 24, 'PHP', 4.3)]
    [('Ivan', 26, 'Python', 4.8)]
    """


def test_2():
    u1 = University('Urban')
    names = ['Ирина', 'Инесса', 'Ингеборга', 'Изабелла']
    for name in names:
        u1.add_student(name, random.randint(18, 50))
    for i in range(1, len(names) + 1):
        u1.add_grade(i, 'Python', random.randint(30, 50) / 10)
        u1.add_grade(i, 'PHP', random.randint(30, 50) / 10)
    pprint(u1.get_students())
    pprint(u1.get_students('Python'))
    """
    Консоль:
    [('Ирина', 26, 'Python', 4.0),
     ('Ирина', 26, 'PHP', 3.5),
     ('Инесса', 41, 'Python', 3.1),
     ('Инесса', 41, 'PHP', 4.4),
     ('Ингеборга', 20, 'Python', 4.1),
     ('Ингеборга', 20, 'PHP', 3.8),
     ('Изабелла', 48, 'Python', 4.2),
     ('Изабелла', 48, 'PHP', 3.0)]
    [('Ирина', 26, 'Python', 4.0),
     ('Инесса', 41, 'Python', 3.1),
     ('Ингеборга', 20, 'Python', 4.1),
     ('Изабелла', 48, 'Python', 4.2)]
    """


if __name__ == '__main__':
    # test_1()
    test_2()
