import potentioReadRoter
import fanRotate
import tempReadVal
import fanOn
import potentioReadSpeed
import fanSpeed
import queue_manager as queue
import logic


def start():

    qman = queue.QueueManager()

    threadLogic = logic.Logic(qman)
    threadLogic.start()

    threadPotPut = potentioReadRoter.PotentioReader(qman)
    threadPotPut.start()

    threadPotGet = fanRotate.FanRotate(qman)
    threadPotGet.start()

    threadTempPut = tempReadVal.TempReadVal(qman)
    threadTempPut.start()

    threadTempGet = fanOn.FanOn(qman)
    threadTempGet.start()

    threadSpeedPut = potentioReadSpeed.PotentioSpeedReader(qman)
    threadSpeedPut.start()

    threadSpeedGet = fanSpeed.FanSpeed(qman)
    threadSpeedGet.start()

start()
