# coding=utf-8
import threading
from time import sleep, ctime
sec = [5, 10]


def loop(nloop, nesc, name=''):
    print "start run", nloop, 'at :', ctime()
    print sleep(nesc)
    print "run done", nloop, "at :", ctime()


def main():
    print "start......."
    loops = range(len(sec))
    threads = []

    print "************单线程"
    for i in loops:
        print 'staring/.......', loop.__name__, "at: ", ctime()
        loop(i, sec[i])
        print "finshed ..........."
    print "************单线程结束"
    for i in loops:
        t = threading.Thread(target=loop, args=(i, sec[i], loop.__name__))

        threads.append(t)
    for i in loops:
        threads[i].start()
    for i in loops:
        threads[i].join()

    print 'All run Done:'

if __name__ == '__main__':
    main()