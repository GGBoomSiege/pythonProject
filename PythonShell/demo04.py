import threading

def worker(num):
    print('Worker %d started' % num)
    # 执行任务
    for i in range(10000000):
        pass
    print('Worker %d finished' % num)

if __name__ == '__main__':
    # 创建 5 个线程
    threads = []
    for i in range(5):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()
