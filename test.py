import time
from threading import Thread

class Test(Thread):
    
    def __init__(self):
        Thread.__init__(self)
        self._run = True

    def run(self):
        while self._run:
            print('hi')
            time.sleep(1)

    def stop(self):
        self._run = False

if __name__ == '__main__':
    thread = Test()
    thread.start()
    #thread.join()
    print('back in main')
    time.sleep(4)
    thread.stop()
    print('yo')

