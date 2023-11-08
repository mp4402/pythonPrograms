"""
https://nrsyed.com/2018/07/05/multithreading-with-opencv-python-to-improve-video-processing-performance/
https://realpython.com/python-concurrency/
https://realpython.com/intro-to-python-threading/#starting-a-thread
"""

from video import CountsPerSec, VideoCaptureThread, ImShowThread
import argparse
import cv2 as cv

def img_annotate(img, text, color=(0, 255, 0)):
    """ Annotate an image with text
    """
    cv.putText(img, text,(10, 120), cv.FONT_HERSHEY_SIMPLEX, 3, color)
    return img


def noThreading(source=0):
    """No threading text
    """

    cap = cv.VideoCapture(source)
    cps = CountsPerSec().start()

    while True:
        ret, frame = cap.read()
        if not ret or cv.waitKey(1) == ord("q"):
            break
        
        fps = str(round(cps.freq(),2))
        frame = img_annotate(frame, fps)
       
        cv.imshow("NO_THREAD", frame)
        cps.increment()

def captureThread(source=0):
    """
    """

    capThreaded = VideoCaptureThread(source).start()
    cps = CountsPerSec().start()

    while True:
        frame = capThreaded.frame
        if not capThreaded.ret or cv.waitKey(1) == ord("q"):
            capThreaded.stop()
            break
        fps = str(round(cps.freq(),2))
        frame = img_annotate(frame, fps)
        
        cv.imshow("CAPTURE_THREAD", frame)
        cps.increment()

def windowThread(source=0):
    """
    Dedicated thread for showing video frames with VideoShow object.
    Main thread grabs video frames.
    """

    cap = cv.VideoCapture(source)
    ret, frame = cap.read()
    win_title = 'THREADED WINDOW'
    winThreaded = ImShowThread(frame, win_title).start()
    cps = CountsPerSec().start()

    while True:
        ret, frame = cap.read()
        if not ret or winThreaded.stopped:
            winThreaded.stop()
            break
        fps = str(round(cps.freq(),2))
        frame = img_annotate(frame, fps)
        winThreaded.frame = frame
        cps.increment()


def threadBoth(source=0):
    """
    Dedicated thread for grabbing video frames with VideoGet object.
    Dedicated thread for showing video frames with VideoShow object.
    Main thread serves only to pass frames between VideoGet and
    VideoShow objects/threads.
    """

    video_getter = VideoCaptureThread(source).start()
    video_shower = ImShowThread(video_getter.frame,'CAPTURE AND WINDOW THREAD').start()
    cps = CountsPerSec().start()

    while True:
        if video_getter.stopped or video_shower.stopped:
            video_shower.stop()
            video_getter.stop()
            break

        frame = video_getter.frame
        fps = str(round(cps.freq(),2))
        frame = img_annotate(frame, fps)
        video_shower.frame = frame
        cps.increment()

if __name__ == '__main__':

    filename = "C:/GitHub/pythonPrograms/computerVision2023/clases/imagenes/maldives.mp4"
    # src = filename
    src = 0
    
    
    # noThreading(src)

    # captureThread(src)
    # windowThread(src)
    threadBoth(src)