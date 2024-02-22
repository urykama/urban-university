# https://www.youtube.com/watch?v=nqhfJgeeQhs&list=PL6plRXMq5RAAb9gwGqmgAoA-KIr-7CMuz&index=6
import multiprocessing
import time


def getter(pipe):
    out, inp = pipe
    inp.close()
    while True:
        try:
            print('data:', out.recv())
        except:
            break


def setter(sequence, input_c):
    for item in sequence:
        time.sleep(0.4)
        input_c.send(item)


if __name__ == '__main__':
    output_c, input_c = multiprocessing.Pipe()
    pr = multiprocessing.Process(target=getter, args=((output_c, input_c),))
    pr.start()
    print('Процесс запущен')
    setter([1, 2, 3, 4, 5], input_c)
    setter(list(range(10)), input_c)
    output_c.close()
    input_c.close()
    print(pr.is_alive())
    print(pr.pid)
    pr.join()
    print('EXIT')
