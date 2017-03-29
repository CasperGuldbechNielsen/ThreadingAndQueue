import threading
import queue as Q
import sys
import RPi.GPIO as GPIO


class FanRotate(threading.Thread):

    def __init__(self, qman):
        threading.Thread.__init__(self)
        self.q_name = "fanRotateQueue"
        self.qman = qman

        GPIO.setmode(GPIO.BCM)
        self.StepPins = [6, 13, 19, 26]

        for pin in self.StepPins:
            print("Setup pins")
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, False)

        self.Seq = [[1, 0, 0, 1], [1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1],
               [1, 0, 0, 1], [1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1],
               [1, 0, 0, 1], [1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1],
               [1, 0, 0, 1], [1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1],
               [1, 0, 0, 1], [1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1],
               [1, 0, 0, 1], [1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1],
               [1, 0, 0, 1], [1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1],
               [1, 0, 0, 1], [1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1]]

        self.StepCount = len(self.Seq)
        self.StepDir = 0
        self.StepCounter = 0

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
        if (str(msg).__contains__("value='1'")):
            self.StepDir = 1
        elif (str(msg).__contains__("value='-1'")):
            self.StepDir = -1
        else:
            self.StepDir = 0

        for pin in range(0, 4):
            xpin = self.StepPins[pin]
            if self.Seq[self.StepCounter][pin] != 0:
                GPIO.output(xpin, True)
            else:
                GPIO.output(xpin, False)

        self.StepCounter += self.StepDir

        if (self.StepCounter >= self.StepCount):
            self.StepCounter = 0
            self.StepDir = 0
        if (self.StepCounter < 0):
            self.StepCounter = self.StepCount + self.StepDir
            self.StepDir = 0
