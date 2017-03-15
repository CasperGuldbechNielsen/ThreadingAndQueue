import queue


class QueueManager:

    def __init__(self):
        # Create input queue
        self.inputQueue = queue.Queue()

        # Create outbound queues
        self.fanRotateQueue = queue.Queue()
        self.fanRPMQueue = queue.Queue()
        self.fanStateQueue = queue.Queue()

    def load_queue(self, load_value, q_name):
        self.get_queue(q_name).put(load_value)
        print("Loaded message: {0} on {1}".format(load_value, q_name))

    def read_queue(self, q_name):
        while not (self.get_queue(q_name).empty()):
            print("Removed: {0} from {1}".format(self.get_queue(q_name).get(), q_name))

    def get_queue(self, q_name):
        if ( q_name == "inputQueue" ):
            return self.inputQueue
        elif ( q_name == "fanRotateQueue" ):
            return self.fanRotateQueue
        elif ( q_name == "fanRPMQueue" ):
            return self.fanRPMQueue
        elif ( q_name == "fanStateQueue" ):
            return self.fanStateQueue
        else:
            print("LOL")
            return 0
