#!usr/bin/env python2

from __future__ import print_function

import time
import pigpio
import wavePWM

from subprocess import call

PIN = 18

def main():
    print("start")

    pi = pigpio.pi()

    if not pi.connected:
        print("pi not connected")
        exit(0)

    pwm = wavePWM.PWM(pi)

    # set frequency to 50 hz, or 1 cycle/20 ms
    pwm.set_frequency(50)
    #pwm.set_cycle_time(20000)
    print("cycle len: {}".format(pwm.get_cycle_length()))

    # 1500 micros is 1.5 millis, which is neutral on servo
    for m in (1000, 1500, 2000):
        print("micros: {}".format(m))
        call(["pigs", "s", "{}".format(PIN), "{}".format(m)])
        
        #pwm.set_pulse_start_and_length_in_micros(PIN, 0, m)

        # update to send data to gpio
        #pwm.update()

        time.sleep(3)

    print("done")

    call(["pigs", "s", "{}".format(PIN), "{}".format(0)])

    pwm.cancel()

    pi.stop()


if __name__ == '__main__':
    main()
