from datetime import datetime
import cv2 as cv
from threading import Thread

class CountsPerSec:
    """ Measure performance in frames per second
    """

    def __init__(self):
        self._start_t = None
        self._frames = 0

    def start(self):
        self._start_t = datetime.now()
        return self
    
    def increment(self):
        self._frames += 1
    
    def freq(self):
        elapsed_time = (datetime.now() - self._start_t).total_seconds()

        if elapsed_time > 0:
            f =  self._frames/elapsed_time
        else:
            f = 0

        return f


class VideoCaptureThread:
    """ Threaded VideoCapture from cv2
    """

    def __init__(self, src=0):
        self.cap = cv.VideoCapture(src)
        self.ret, self.frame = self.cap.read()
        self.stopped = False

    def start(self):
        #create thread and start executing
        Thread(target=self.capture, args=()).start()
        return self

    def capture(self):
        while not self.stopped:
            if not self.ret:
                self.stop()
            else:
                self.ret, self.frame = self.cap.read()

    def stop(self):
        self.stopped = True


class ImShowThread:
    """
    """
    
    def __init__(self, frame=None, window_title='Window Thread'):
        self.frame = frame
        self.stopped = False
        self.title = window_title

    def start(self):
        Thread(target=self.show, args=()).start()
        return self

    def show(self):
        cv.namedWindow(self.title, cv.WINDOW_NORMAL)
        while not self.stopped:
            cv.imshow(self.title, self.frame)
            if cv.waitKey(1) == ord("q"):
                self.stopped = True 

    def stop(self):
        self.stopped = True