import RPi.GPIO as GPIO
import time


def main():

    frequency = 200
    repeat_count = 600
    gpio_pin = 18

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(gpio_pin, GPIO.OUT)

    for i in [10, 100, 10, 100]:
        
        if 0 == i:
            on_time = 0
            off_time = (1 / frequency)
        else:
            on_time = (1 / frequency) * (i / 100)
            off_time = (1 / frequency) * (1 - (i / 100))

        for ct in range(repeat_count):
            GPIO.output(gpio_pin, True)
            time.sleep(on_time)
            GPIO.output(gpio_pin, False)
            time.sleep(off_time)
            
    GPIO.cleanup()


if __name__ == '__main__':
    main()
