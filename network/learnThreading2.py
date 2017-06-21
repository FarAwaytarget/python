# coding=utf-8
import threading
from time import sleep, ctime

loops = [2, 4]

class ThreadFunc(object):
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        apply(self.func, self.args)


def loop(nloop, nsec):
    print "Start loop ", nloop, "at", ctime()
    sleep(nsec)
    print "loop ", nloop, "done at :", ctime()


def main():
    print "Start at:", ctime()
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(
            target=ThreadFunc(loop, (i, loops[i]), loop.__name__) # 要传递函数，以及函数参数，或者类，类方法，方法参数
        )
        threads.append(t)
    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print "ALl end:", ctime()


if __name__ == '__main__':
    main()
