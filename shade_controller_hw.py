# Raspberry Pi gpio pin control module for Shade Controller App


from time import sleep
try:
    import RPi.GPIO as gpio
except ImportError:
    import mockGPIO as gpio


gpio.setmode(gpio.BOARD)
gpio.setup(18,gpio.OUT)
gpio.setup(16,gpio.OUT)

def up():
    gpio.output(16,1)
    sleep(0.3)
    gpio.output(16,0)

def down():
    gpio.output(18,1)
    sleep(0.3)
    gpio.output(18,0)
