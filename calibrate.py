import time

NEUTRAL = 1500
DOWN = 200
UP = -200

from blinds import Blinds

def main():
    blinds = Blinds()
    blinds.run_servo(NEUTRAL + UP)
    time.sleep(1)
    blinds.run_servo(NEUTRAL)


if __name__ == '__main__':
   main()
