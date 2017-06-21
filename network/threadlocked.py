#coding=utf-8
import thread
from time import sleep, ctime

loops = [4, 2]
# lock time object

def loop(nloop, nsec, lock):
    print "start x  loop", nloop,  'at: ', ctime(),'\n'
    sleep(nsec)
    print "loop", nloop, 'done at: ', ctime()
    lock.release()

def main():
    print "starting at:", ctime()
    locks = []
    nloops = range(len((loops)))

    for i in nloops:
        lock = thread.allocate_lock()  #creat lock object
        lock.acquire() # get lock ,add lock
        locks.append(lock) # add locks
    # action multithreading
    for i in nloops:
        thread.start_new_thread(loop, (i, loops[i], locks[i]))
    # runloop check locked is unlock
    for i in nloops:
        while locks[i].locked():
            pass
    print 'all end:', ctime()

if __name__ == '__main__':
     main()
