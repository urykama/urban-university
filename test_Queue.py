import multiprocessing
import queue
import random
import threading
import time


def get_text(q):
    val = random.randint(0, 10)
    q.put(str(val))


if __name__ == '__main__':
    # with Pool(5) as p:
    #     print(p.map(f, [1, 2, 3]))
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
