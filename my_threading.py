import threading
import time


class MyThreads(threading.Thread):
    def __init__(self, thread_id, thread_name, delay, read_or_write, queue_name, queue_manager):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.thread_name = thread_name
        self.thread_delay = delay
        self.read_or_write = read_or_write
        self.queue_name = queue_name
        self.q = queue_manager

    def run(self):
        print("Starting thread " + self.thread_name)

        if (self.read_or_write == "read"):
            self.thread_read_queue()
        elif (self.read_or_write == "write"):
            self.thread_load_queue()
        else:
            print("Some error occurred..")

        print("Exiting thread " + self.thread_name)

    def thread_load_queue(self):
        for i in range(0, 1000):
            load_value = "'Value: " + str(i) + " | Date: " + time.ctime() + "'"
            self.q.load_queue(load_value)
            time.sleep(self.thread_delay)

    def thread_read_queue(self):
        while not (self.q.get_queue().empty()):
            self.q.read_queue()
            time.sleep(self.thread_delay)
