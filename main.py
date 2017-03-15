import my_threading
import queue_manager


def start():
    qman = queue_manager.QueueManager()

    thread_load = my_threading.MyThreads(1, "LoadThread", 2, "write", "Test", qman, "inputQueue")
    thread_read = my_threading.MyThreads(2, "ReadThread", 4, "read", "Test", qman, "inputQueue")
    thread_load1 = my_threading.MyThreads(1, "LoadThread", 2, "write", "Test", qman, "fanRotateQueue")
    thread_read1 = my_threading.MyThreads(2, "ReadThread", 4, "read", "Test", qman, "fanRotateQueue")
    thread_load2 = my_threading.MyThreads(1, "LoadThread", 2, "write", "Test", qman, "fanRPMQueue")
    thread_read2 = my_threading.MyThreads(2, "ReadThread", 4, "read", "Test", qman, "fanRPMQueue")
    thread_load3 = my_threading.MyThreads(1, "LoadThread", 2, "write", "Test", qman, "fanStateQueue")
    thread_read3 = my_threading.MyThreads(2, "ReadThread", 4, "read", "Test", qman, "fanStateQueue")

    thread_load.start()
    thread_read.start()
    thread_load1.start()
    thread_read1.start()
    thread_load2.start()
    thread_read2.start()
    thread_load3.start()
    thread_read3.start()

start()
