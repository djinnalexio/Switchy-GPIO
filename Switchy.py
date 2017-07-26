#!/usr/bin/python
# -*- coding: utf-8 -*-

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

color = (blue, green, red, white, white2, yellow)

def turnON(color):
	"Turns on lights"
	Pin.output(color,Pin.HIGH)
	print "The %s light(s) is now on." % str(color)
	time.sleep(1.5)

def turnOFF(color):
	"Turns off lights"
	Pin.output(color,Pin.LOW)
	print "The %s light(s) is now off." % str(color)
	time.sleep(1.5)

def blink(color, duration):
	"Makes lights blink for <duration> seconds"
	step = 1.0 / 6.0
	print "The %s light(s) will be blinking for %i seconds." % (str(color), duration)
	print "		Starting in",
	for i in range(0,2):
		print 3 - i
	count = range(0,duration)
	for i in count:
		turnON(color)
		time.sleep(step)
		turnOFF(color)
		time.sleep(step)
		turnON(color)
		time.sleep(step)
		turnOFF(color)
		time.sleep(step)
		turnON(color)
		time.sleep(step)
		turnOFF(color)
		time.sleep(step)
	print "Well, 'looks like that's it! anything else?"

#def passing_shadow(duration):

#def alt_blink(duration):

#def countdown(duration):



#Start of the app


print ("""
☻ ☼ ☽ ☾ ♠ ♡ ♢ ♣ ♤ ♥ ♦ ♧ ♨ ♩ ✙ ✈ ✉ ✌ ✁ ✎ ✐ ❀ ✰ ❁ ☻ ☼ ☽ ☾ ♠ ♡ ♢ ♣ ♤ ♥ ♦ ♧ ♨ ♩ 

	Hello friend. Nice to meet you! I'm Switchy!^‿^""")

raw_input()

print ("""
	I bet you're here because you wanna know how to
	  turn on the lights connected to the Pi!^‿^""")

raw_input()

print ("""
	If I'm right, then don't worry 'cause you're at
	              the right place!^‿^""")

raw_input()

print("""
	^‿^You see, I'm the application that allows you
	          to control those lights.""")

raw_input()

username = raw_input("""
		But before we get to business,
		   may I have your name? •‿•
			◊""")


