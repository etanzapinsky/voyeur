#!usr/bin/env python2

import time

from subprocess import call

PIN = 18
FORWARDS = 1000
STOP = 1500
BACKWARDS = 2000

# time in seconds
SERVO_RUNTIME = 5

class Blinds:
    def __init__(self):
        self.opened = False
        self.closed = False
        self.moving = False

    def run_servo(self, direction):
        call(["pigs", "s", "{}".format(PIN), "{}".format(direction)])
        
    def open(self):
        # set that we're no longer closed
        self.closed = False
        
        if self.opened or self.moving:
            return

        print('open')

        # set that we're moving
        self.moving = True

        self.run_servo(BACKWARDS)

        # sleep to let the servo move
        time.sleep(SERVO_RUNTIME)

        self.run_servo(STOP)

        # set that we've finished moving
        self.moving = False

        # set that we're open
        self.opened = True
 
    def close(self):
        # set that we're no longer open
        self.opened = False

        if self.closed or self.moving: 
            return

        print('close')

        # set that we're moving
        self.moving = True
        
        self.run_servo(FORWARDS)

        # sleep to let the servo move
        time.sleep(SERVO_RUNTIME)

        self.run_servo(STOP)

        # set that we've finished moving
        self.moving = False

        # set that we're closed
        self.closed = True
       
