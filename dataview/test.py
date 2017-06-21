#coding=gbk
import thread, time, random

def func():
    for i in range(5):
        print('func')
        time.sleep(1)
    thread.exit()