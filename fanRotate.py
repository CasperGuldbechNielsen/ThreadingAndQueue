import xmlFormatForQueues as Xml
import threading
import queue as Q
import time


class FanRotate(threading.Thread):

    def __init__(self, qman):
        threading.Thread.__init__(self)
        self.threadName = "LoadInputQueueThread"
        form = Xml.unParsedValueFormat
        self.q_name = "fanRotateQueue"
        self.qman = qman

    def run(self):
        self.read()

    def read(self):
        while (True):
            try:
                msg = self.qman.read_queue(self.q_name)
                print("\n\nRemoved message: \n{0} \nfrom {1}".format(msg, self.q_name))
            except Q.Empty:
                print("Queue {0} is empty..".format(self.q_name))

