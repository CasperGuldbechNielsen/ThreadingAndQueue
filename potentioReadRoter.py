import threading
import RPi.GPIO as GPIO


class PotentioReader(threading.Thread):

    def __init__(self, qman):
        threading.Thread.__init__(self)
        self.q_name = "inputQueue"
        self.qman = qman

        # Rotary Encoder stuff
        self.clk = 17
        self.dt = 18

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        self.counter = 0
        self.oldCounter = 0
        self.clkLastState = GPIO.input(self.clk)

    def run(self):
        self.load()

    def load(self):
        while (True):
            load_value = self.read()
            self.qman.load_queue(load_value, self.q_name)

    def read(self):
        clkState = GPIO.input(self.clk)
        dtState = GPIO.input(self.dt)
        if clkState != self.clkLastState:
            if dtState != clkState:
                self.counter += 1
            else:
                self.counter -= 1
            print(self.counter)
            self.clkLastState = clkState

        if (self.counter > self.oldCounter):
            StepDir = 1
        elif (self.counter < self.oldCounter):
            StepDir = -1
        else:
            StepDir = 0

        self.oldCounter = self.counter
        return "<xmldoc>" + "\n\t<component value='rotor'>" + "\n\t\t<value='{0}'/>".format(StepDir) + "\n\t</component>" + "\n</xmldoc>"
