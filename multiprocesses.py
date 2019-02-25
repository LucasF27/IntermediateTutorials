import multiprocessing
import time

def spawn(num):
    print('Spawned {}'.format(num))
    # time.sleep(1)

if __name__ == '__main__':
    for i in range(100):
        p = multiprocessing.Process(target=spawn, args=(i,))
        p.start()
        p.join() # wait for processes