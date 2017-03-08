import my_threading
import my_queue


def start():
    queue_manager = my_queue.MyQueue()

    thread_load = my_threading.MyThreads(1, "LoadThread", 2, "write", "Test", queue_manager)
    thread_read = my_threading.MyThreads(2, "ReadThread", 4, "read", "Test", queue_manager)

    thread_load.start()
    thread_read.start()

start()
