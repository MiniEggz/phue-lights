from threading import Thread
import datetime

class WakeyThread(Thread):

    # get bridge, light name and wake_time and set flag
    def __init__(self, b, light_name, wake_time):
        Thread.__init__(self)
        self.b = b
        self.light_name = light_name
        self.wake_time = wake_time
        self._run = True

    # wait until time and then turn light on
    def run(self):
        while self._run:
            if datetime.datetime.now() > self.wake_time:
                self.b.set_light(self.light_name, 'on', True)
                self._run = False
    
    # change flag to stop the thread
    def stop(self):
        self._run = False