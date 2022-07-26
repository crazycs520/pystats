import os
import psutil
import _thread

MB = 1024 * 1024
GB = 1024 * 1024 * 1024

def consume_memory(size):
    """
    创建一个大小为 size 的字符串，并返回
    """
    return 'a' * size

def consume_cpu(num):
    """
    消耗 CPU 资源
    """
    while num > 0:
        num -= 1
    
def consume_resource():
    count = 10000
    while count > 0:
        consume_memory(50 * MB)
        consume_cpu(10e7)
        count -= 1

if __name__ == '__main__':
    # 创建一个线程模拟消耗资源
    _thread.start_new_thread( consume_resource, () )

    for i in range(100): 
        print('-'*100)
        # 获取当前整个系统的 CPU 使用率
        print('System CPU usage is: {}%'.format( psutil.cpu_percent(interval=1)))
        # 获取当前整个系统的内存已使用大小，可用大小，以及使用率
        virtual_memory = psutil.virtual_memory()
        print('System RAM memory used: {} GB, available: {} GB, used percent: {}'.format( virtual_memory[3]/GB, virtual_memory[1]/GB, virtual_memory[2]))

        pid = os.getpid()
        process = psutil.Process(pid)
        print('pid {} process CPU usage: {}%'.format( pid, process.cpu_percent(interval=1)))

        # 获取当前进程的内存使用大小
        memory_info = process.memory_info()
        print('pid {} process memory used: {} MB'.format( pid, memory_info[0]/MB))
        print('\n')
