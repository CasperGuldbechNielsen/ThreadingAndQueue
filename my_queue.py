import queue


class MyQueue:

    def __init__(self):
        self.queue_name = queue.Queue()
        self.load = []

    def load_queue(self, load_value):
        self.queue_name.put(load_value)
        print("Loaded message: {0} on queue".format(load_value))

    def read_queue(self):
        while not (self.queue_name.empty()):
            print("Removed: {0} from queue".format(self.queue_name.get()))

    def get_queue(self):
        return self.queue_name
