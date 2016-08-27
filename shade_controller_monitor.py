# Persistent rule-monitoring module for Shade Controller App

import time, threading
from datetime import datetime, time, timedelta
import shade_controller_hw as hw


class Monitor(object):
    def __init__(self):
        self.TIMES = {0:time(7,30),1:time(19,30)}
        self.timer = threading.Timer(1,None)

    def manualup(self):
        hw.up()

    def manualdown(self):
        hw.down()

    def cleanup(self):
        if self.timer.is_alive():
            print("cancelling autochange timer")
            self.timer.cancel()
        hw.cleanup()

    def autochange(self):
        now = datetime.today()
        mdist = (datetime.combine(now.date(),self.TIMES[0])-now).seconds # seconds until next morning
        ndist = (datetime.combine(now.date(),self.TIMES[1])-now).seconds  # seconds until next evening
        interval = mdist if mdist < ndist else ndist # select shorter wait
        interval = interval + 1 # prevent running too quickly
        hw.down() if mdist < ndist else hw.up() # if before morning time, make sure shade is down; if before evening time, make sure shade is up
        self.timer = threading.Timer(interval, self.autochange) # set timer again when finished
        print("starting autochange timer for: " + str(interval))
        self.timer.start()