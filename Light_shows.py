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

colors = (blue, green, red, white, white2, yellow)

def moving_shadow():
	"Pattern 1: moving light"

	duration = raw_input("\n\tFor how long do you want the pattern to run for? (in seconds)\n\t\t>")
	if duration.isdigit():
		duration = int(duration)
	else:
		print ("""
				✖﹏✖
		✖﹏✖ Sorry, I didn't get what you meant... ✖﹏✖
				✖﹏✖

	""")
		time.sleep(1)
		return
	
	speed = raw_input("\n\tChoose a speed for the lights•‿•\n\t\t>")
	if speed.isdigit() :
		inter = (1/3.0) / int(speed)
	else:
		print ("""
				✖﹏✖
		✖﹏✖ Sorry, I didn't get what you meant... ✖﹏✖
				✖﹏✖

	""")
		time.sleep(1)
		return
	
	print "\n\tThe light show will run for %s seconds.\n\tSpeed: %s." % (duration, speed)

	time.sleep(1)
	Pin.output(colors, True)

	print "		•‿•Starting in:"
	time.sleep(1)	
	for i in range(0,3):
		print "\t\t\t",3 - i
		time.sleep(1)

	stp = time.time() ; etp = time.time() + duration# stp/etp = starting / ending time pattern
	while time.time() < etp: 
		print (int(time.time() - stp))# elased time = current time - time start blink
		Pin.output(white2,False)
		
		time.sleep(inter)
		Pin.output(white2,True)
		Pin.output(green,False)
		
		time.sleep(inter)
		Pin.output(green,True)
		Pin.output(blue,False)
		
		time.sleep(inter)
		Pin.output(blue,True)
		Pin.output(red,False)
		
		time.sleep(inter)
		Pin.output(red,True)
		Pin.output(yellow,False)
		
		time.sleep(inter)
		Pin.output(yellow,True)
		Pin.output(white,False)
		
		time.sleep(inter)
		Pin.output(white,True)
	
	time.sleep(1)
	Pin.output(colors, False)


def moving_shadow2():
	"Pattern 1: moving light"

	duration = raw_input("\n\tFor how long do you want the pattern to run for? (in seconds)\n\t\t>")
	if duration.isdigit():
		duration = int(duration)
	else:
		print ("""
				✖﹏✖
		✖﹏✖ Sorry, I didn't get what you meant... ✖﹏✖
				✖﹏✖

	""")
		time.sleep(1)
		return
	
	speed = raw_input("\n\tChoose a speed for the lights•‿•\n\t\t>")
	if speed.isdigit() :
		inter = (1/3.0) / int(speed)
	else:
		print ("""
				✖﹏✖
		✖﹏✖ Sorry, I didn't get what you meant... ✖﹏✖
				✖﹏✖

	""")
		time.sleep(1)
		return
	
	print "\n\tThe light show will run for %s seconds.\n\tSpeed: %s." % (duration, speed)

	time.sleep(1)
	Pin.output(colors, True)

	print "		•‿•Starting in:"
	time.sleep(1)	
	for i in range(0,3):
		print "\t\t\t",3 - i
		time.sleep(1)

	stp = time.time() ; etp = time.time() + duration# stp/etp = starting / ending time pattern
	while time.time() < etp: 
		print (int(time.time() - stp))# elased time = current time - time start blink
		Pin.output(white2,False)
		
		time.sleep(inter)
		Pin.output(white,True)
		Pin.output(green,False)
		
		time.sleep(inter)
		Pin.output(white2,True)
		Pin.output(blue,False)
		
		time.sleep(inter)
		Pin.output(green,True)
		Pin.output(red,False)
		
		time.sleep(inter)
		Pin.output(blue,True)
		Pin.output(yellow,False)
		
		time.sleep(inter)
		Pin.output(red,True)
		Pin.output(white,False)
		
		time.sleep(inter)
		Pin.output(yellow,True)
	
	time.sleep(inter)	
	Pin.output(white,True)
	
	time.sleep(1)
	Pin.output(colors, False)
	
print("""
	Here are the available light shows:

1:Moving Shadow

2:Moving Shadow 2

		^‿^ So, what do you want to do?
			""")
			
l_s = raw_input("""			Type a number here ->""")


if l_s == '1':#Moving Shadow
	moving_shadow()

elif l_s == '2':#Moving Shadow2
	moving_shadow2()

else:#not defined
	time.sleep(1)
	print("""
				✖﹏✖
		✖﹏✖ Sorry. I didn't understand what you typed. ✖﹏✖
				✖﹏✖

	""")
	time.sleep(1)
