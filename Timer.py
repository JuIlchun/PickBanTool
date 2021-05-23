import threading


def starttimer(bool):
    timer=threading.Timer(27,starttimer,args=(False))
    timer.start()

    if bool == True:
        timer.cancel()