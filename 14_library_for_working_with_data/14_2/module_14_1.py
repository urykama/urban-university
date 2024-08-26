import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS Users')
# Инструкция SQL DROP TABLE IF EXISTS используется для удаления таблицы из базы данных, если таблица существует.
# Если таблица не существует, то инструкция выдает предупреждение.

cursor.execute(
    '''
    CREATE TABLE Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
    )
    ''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users(email)')

for i in range(1, 11, 1):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (f'User{i}', f'example{i}@gmail.com', str(i * 10), '1000'))

for i in range(1, 11, 2):
    cursor.execute('UPDATE Users SET balance = ? WHERE username == ?', ('500', f'User{i}'))

for i in range(1, 11, 3):
    cursor.execute('DELETE FROM Users WHERE username == ?', (f'User{i}',))

cursor.execute('SELECT * FROM Users WHERE age != 60')
users = cursor.fetchall()

connection.commit()
connection.close()

if __name__ == '__main__':
    for user in users:
        print('Имя: {} | Почта: {} | Возраст: {} | Баланс: {}'.format(*user[1:]))
