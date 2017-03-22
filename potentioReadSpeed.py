import threading


class PotentioSpeedReader(threading.Thread):

    def __init__(self, qman):
        threading.Thread.__init__(self)
        self.q_name = "inputQueue"
        self.qman = qman

    def run(self):
        self.load()

    def load(self):
        while (True):
            load_value = self.read()
            self.qman.load_queue(load_value, self.q_name)

    def read(self):
        # read from sensor
        load_value = "<xmldoc>" + "\n\t<component value='fanRPM'>" + "\n\t\t<value='10'/>" + "\n\t</component>" + "\n</xmldoc>"

        return load_value
