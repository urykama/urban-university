from threading import Thread
from time import sleep


def printNumber():
    for i in range(1, 11):
        print(i)
        sleep(1)


def printChar():
    listing = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
    for i in listing:
        print(i)
        sleep(1)


threadNumber = Thread(target=printNumber)
threadChar = Thread(target=printChar)
threadNumber.start()
threadChar.start()
threadNumber.join()
threadChar.join()
