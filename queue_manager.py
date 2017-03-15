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
        print("\n\nLoaded message: \n{0} \non {1}".format(load_value, q_name))

    def read_queue(self, q_name):
        return self.get_queue(q_name).get()

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
