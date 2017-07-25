import RPi.GPIO as Pin
import time
Pin.setmode(Pin.BCM)
Pin.setwarnings(False)

blue=25
Pin.setup(blue, Pin.OUT)
green=24
Pin.setup(green, Pin.OUT)
red=12
Pin.setup(red, Pin.OUT)
white=21
Pin.setup(white, Pin.OUT)
white2=18
Pin.setup(white2, Pin.OUT)
yellow=16
Pin.setup(yellow, Pin.OUT)

def turnON(color):
	Pin.output(color,Pin.HIGH)

def turnOFF(color):
	Pin.output(color,Pin.LOW)

def blink(color, duration):
	count = range(0,duration)
	for i in count:
		turnON(color)
		time.sleep(0.2)
		turnOFF(color)
		time.sleep(0.2)
		turnON(color)
		time.sleep(0.2)
		turnOFF(color)
		time.sleep(0.2)
		turnON(color)
		time.sleep(0.2)
	print "end"

def passing_shadow(duration):

def alt_blink(duration):

def countsec(duration):
