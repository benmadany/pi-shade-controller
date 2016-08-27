# Raspberry Pi gpio pin control module for Shade Controller App


from time import sleep
try:
    import RPi.GPIO as gpio
except ImportError:
    import mockGPIO as gpio


UP = 16
DOWN = 18
WAIT = 0.4

#gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(UP,gpio.OUT)
gpio.setup(DOWN,gpio.OUT)

def up():
    print("HW Raise")
    gpio.output(UP,1)
    sleep(WAIT)
    gpio.output(UP,0)

def down():
    print("HW Lower")
    gpio.output(DOWN,1)
    sleep(WAIT)
    gpio.output(DOWN,0)

def cleanup():
    print("HW Cleanup")
    gpio.cleanup()