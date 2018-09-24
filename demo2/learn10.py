# Process进程

#
# from multiprocessing import Process
# import os
# # 子进程需要执行的代码
# def run(name):
#     print('Run child process %s (%s)...' %(name,os.getpid()))
# if __name__ == '__main__':
#     print('Parent process %s.' %os.getpid())
#     p=Process(target=run,args=('test',))  #创建实例
#     print('Child process will start')
#     p.start()
#     p.join()             #等待子进程
#     print('Child process end')


# Pool进程
# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
# from multiprocessing import Pool
# import os,time,random
# def task(name):
#     print('Run task %s (%s)...' %(name,os.getgid()))
#     start=time.time()
#     time.sleep(random.random()*3)
#     end=time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p=Pool(4)
#     for i in range(5):
#         p.apply_async(task,args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')
# 进程间通信
# Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。

# 我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据。
from multiprocessing import Process, Queue
# import os, time, random
#
#
# # 写数据进程执行的代码:
# def write(q):
#     print('Process to write: %s' % os.getpid())
#     for value in ['A', 'B', 'C']:
#         print('Put %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random())


#
# # 读数据进程执行的代码:
# def read(q):
#     print('Process to read: %s' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue.' % value)
#
# if __name__=='__main__':
#     # 父进程创建Queue，并传给各个子进程：
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     # 启动子进程pw，写入:
#     pw.start()
#     # 启动子进程pr，读取:
#     pr.start()
#     # 等待pw结束:
#     pw.join()
#     # pr进程里是死循环，无法等待其结束，只能强行终止:
#     pr.terminate()
# # 线程
# import time, threading
#
#
# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n<5:
#         n=n+1
#         print('thread %s>>%s' % (threading.current_thread().name,n))
#         time.sleep(1)
#     print('thread %s end'% threading.current_thread().name)
# #
# if __name__ == '__main__':
#
#      print('threading %s is running...' % threading.current_thread().name)
#      t = threading.Thread(target=loop, name='LoopThread')
#      t.start()
#      t.join()
#      print('Thread %s end' % threading.current_thread().name)
#ThreadLocal
import threading
                             # 创建全局ThreadLocal对象:
local_school=threading.local()

def process_student():
    std=local_school.student
    print('Hello,%s(in %s)'% (std,threading.current_thread().name))
def process_thread(name):
                             # 绑定ThreadLocal的student:
    local_school.student=name
    process_student()
if __name__ == '__main__':
    t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
    t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
    t1.start()
    t2.start()
    t1.join()
    t2.join()










