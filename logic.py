import xmlFormatForQueues as Xml
import threading
import queue as Q
import time


class Logic(threading.Thread):

    def __init__(self, qman):
        threading.Thread.__init__(self)
        self.threadName = "LoadInputQueueThread"
        form = Xml.unParsedValueFormat
        self.q_in_name = "inputQueue"
        self.qman = qman
        self.msg = None

    def run(self):
        self.read()

    def read(self):
        while (True):
            try:
                self.msg = self.qman.read_queue(self.q_in_name)
                self.load()
            except Q.Empty:
                print("Queue {0} is empty..".format(self.q_in_name))

    def load(self):
        if ( self.msg is not None ):
            if ( str(self.msg).__contains__('rotor') ):
                self.qman.load_queue(self.msg, "fanRotateQueue")
            elif ( str(self.msg).__contains__('temp') ):
                self.qman.load_queue(self.msg, "fanStateQueue")
            elif (str(self.msg).__contains__('fanRPM')):
                self.qman.load_queue(self.msg, "fanRPMQueue")
            else:
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            self.msg = None
