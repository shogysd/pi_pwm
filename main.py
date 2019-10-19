import RPi.GPIO as GPIO
import time


def main():

    frequency = 200
    cycle_time = 500
    gpio_pin = 18

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(gpio_pin, GPIO.OUT)

    for i in [20, 99, 20, 99]: #range(20, 100):
        on_time = (1 / frequency) * (i / 100)
        off_time = (1 / frequency) * ((99 - i) / 100)

        for ct in range(cycle_time):
            GPIO.output(gpio_pin, True)
            time.sleep(on_time)
            GPIO.output(gpio_pin, False)
            time.sleep(off_time)


if __name__ == '__main__':
    main()
