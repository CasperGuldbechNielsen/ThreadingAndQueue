import threading
import queue as Q


class FanOn(threading.Thread):

    def __init__(self, qman):
        threading.Thread.__init__(self)
        self.q_name = "fanStateQueue"
        self.qman = qman

    def run(self):
        self.read()

    def read(self):
        while (True):
            try:
                msg = self.qman.read_queue(self.q_name)
                self.rotate(msg)
            except Q.Empty:
                print("Queue {0} is empty..".format(self.q_name))

    def rotate(self, msg):
        # Have logic to rotate here...
        print("\n")
