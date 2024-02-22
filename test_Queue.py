import multiprocessing
import queue
import random
import threading
import time


def test():
    while True:
        print(f'{multiprocessing.current_process()} - {time.time()}')
        time.sleep(1)


multiprocessing.Process(target=test, name='prc-1').start()
print('Процесс запущен')


# data = threading.local()  # создает переменную для каждого потока свою
#
# def get():
#     print(data.value)
# def t1():
#     data.value = 111
#     get()
# def t2():
#     data.value = 222
#     get()
# threading.Thread(target=t1).start()
# threading.Thread(target=t2).start()


# def test_Timer():
#     while True:
#         print('test')
#         time.sleep(1)
#
# thr = threading.Timer(5, test_Timer)
# thr.daemon = True
# thr.start()
# # for _ in range(3):
# for _ in range(6):
#     print(f'{threading.current_thread().name}')
#     time.sleep(1)
# thr.cancel()
# print("finish")


# value = 0
# # locker = threading.Lock()  # Lock можно разблокировать из любой области
# locker = threading.RLock()  # RLock можно разблокировать только из потока который заблокировал
#
# def inc_value():
#     global value
#     for _ in range(100):
#         # locker.acquire()
#         # value += 1
#         # # time.sleep(0.3)
#         # print(value)
#         # locker.release()
#         with locker:
#             value += 1
#             # time.sleep(0.3)
#             print(value)
#
#
# if __name__ != '__main__':
#     for _ in range(50):
#         threading.Thread(target=inc_value).start()


def get_data1(data, value):
    for _ in range(value):
        print(f'[{threading.current_thread().name}] - {data}')
        time.sleep(0.3)


if __name__ != '__main__':
    thr_list = []
    for i in range(3):
        thr = threading.Thread(target=get_data1, args=(str(time.time()), (i + 1) * 10,), name=f'thr-{i}')
        # thr.setDaemon(True)
        thr.daemon = True
        # thr = threading.Thread(target=get_data1, args=(str(time.time()), (i + 1) * 10,), name=f'thr-{i}', daemon=True)

        thr_list.append(thr)
        thr.start()
    print(thr_list)
    # for i in thr_list:
    #     i.join()
    for i in range(25):
        print(f'[{threading.current_thread().name}] - {i}')
        time.sleep(0.3)
        if i % 10 == 0:
            print('threading.active_count():', threading.active_count())
            print('threading.enumerate():', threading.enumerate())
            print('thr.is_alive():', thr.is_alive())


def get_data(data):
    while True:
        print(f'[{threading.current_thread().name}] - {data}')
        time.sleep(0.3)


if __name__ != '__main__':
    thr = threading.Thread(target=get_data, args=(str(time.time()),), name='thr-1')
    thr.start()
    for i in range(100):
        print(f'[{threading.current_thread().name}] - {i}')
        time.sleep(0.3)
        if i % 10 == 0:
            print('threading.active_count():', threading.active_count())
            print('threading.enumerate():', threading.enumerate())
            print('thr.is_alive():', thr.is_alive())


def get_text(q):
    val = random.randint(0, 10)
    q.put(str(val))


if __name__ != '__main__':
    queue = multiprocessing.Queue()
    pr_list = []
    for _ in range(10):
        pr = multiprocessing.Process(target=get_text, args=(queue,))
        pr_list.append(pr)
        pr.start()
    for i in pr_list:
        i.join()
    for elem in iter(queue.get, None):
        print(elem)

# for i in range(5):
#     q.put(i)
# while not q.empty():
#     print(q.get(), end=' ')


# q.put(5)
# print(q.get())
# # print(q.get())
# print(q.empty())


# from queue import Queue
# from random import randint
# from threading import Thread
# from time import sleep
#
#
#
# def writeQ(queue):
#     print()
#     print('producing object for Q...')
#     queue.put('xxx', 1)
#     print("size now", queue.qsize())
#
#
# def readQ(queue):
#     val = queue.get(1)
#     print('consumed object from Q... size now')
#     queue.qsize()
#
#
# def writer(queue, loops):
#     for i in range(loops):
#         writeQ(queue)
#         sleep(randint(1, 3))
#
#
# def reader(queue, loops):
#     for i in range(loops):
#         readQ(queue)
#         sleep(randint(2, 5))
#
#
# funcs = [writer, reader]
# nfuncs = range(len(funcs))
#
#
# def main():
#     nloops = randint(2, 5)
#     q = Queue(32)
#
#     threads = []
#     for i in nfuncs:
#         t = Thread(funcs[i], q, nloops, funcs[i].__name__)
#         threads.append(t)
#
#     for i in nfuncs:
#         threads[i].start()
#
#     for i in nfuncs:
#         threads[i].join()
#
#     print('all DONE')
#
#
# if __name__ == '__main__':
#     main()
