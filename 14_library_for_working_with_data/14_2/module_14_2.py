import module_14_1
import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute(f'DELETE FROM Users WHERE id == ?', ('6', ))
total_users = cursor.execute('SELECT COUNT(username) FROM Users').fetchone()[0]
all_balances = cursor.execute('SELECT SUM(balance) FROM Users').fetchone()[0]

connection.commit()
connection.close()

if __name__ == '__main__':
    print(all_balances / total_users)