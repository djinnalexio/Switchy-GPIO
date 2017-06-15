#In this file, I will write down all the functions I use

import RPi.GPIO as Pin
import time
Pin.setmode(Pin.BCM)
Pin.setwarnings(False)

white2=18
green=24
blue=8
red=12
yellow=16
white=21
none="none"

def turnON(color):
	Pin.setup(color,Pin.OUT)
	Pin.output(color,Pin.HIGH)

def turnOFF(color):
	Pin.setup(color,Pin.OUT)
	Pin.output(color,Pin.LOW)

def blink(color, blink_time):
	count = range(0,blink_time)
	for i in count:
		print i + 1
		turnON(color)
		time.sleep(0.25)
		turnOFF(color)
		time.sleep(0.25)
		turnON(color)
		time.sleep(0.25)
		turnOFF(color)
		time.sleep(0.25)
	print "end"
