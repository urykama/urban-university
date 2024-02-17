import threading


# Класс BankAccount должен отражать банковский счет с балансом и методами для пополнения и снятия денег.
# Необходимо использовать механизм блокировки,
# чтобы избежать проблемы гонок (race conditions) при модификации общего ресурса.
class BankAccount(threading.Thread):
    def __init__(self, lock, *args, **kwargs):
        super(BankAccount).__init__(*args, **kwargs)
        self.balance = 1000
        self.lock = lock

    def deposit(self, amount):
        # self.balance += amount
        # print(f'Deposited {amount}, new balance is {self.balance}')
        with self.lock:
            self.balance += amount
            print(f'Deposited {amount}, new balance is {self.balance}')

    def withdraw(self, amount):
        # self.balance -= amount
        # print(f'Withdrew {amount}, new balance is {self.balance}')
        with self.lock:
            self.balance -= amount
            print(f'Withdrew {amount}, new balance is {self.balance}')


def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)


def withdraw_task(account, amount):
    for _ in range(5):
        account.withdraw(amount)
        # account = BankAccount()


lock = threading.Lock()
account = BankAccount(lock)
deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
