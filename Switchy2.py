#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as Pin
import time
Pin.setmode(Pin.BCM)
Pin.setwarnings(False)

left=21 #40
Pin.setup(left, Pin.OUT)
yellow=16 #36
Pin.setup(yellow, Pin.OUT)
red=12 #32
Pin.setup(red, Pin.OUT)
blue=25 #22
Pin.setup(blue, Pin.OUT)
green=24 #18
Pin.setup(green, Pin.OUT)
right=17 #11
Pin.setup(right, Pin.OUT)

white=left,right

all = (left, yellow, red, blue, green, right)


color_list = ['all', 'left', 'yellow', 'red', 'blue', 'green', 'right', 'white']

def turnON(color):
	"Turns on lights"
	Pin.output(color,Pin.HIGH)#Instead of 'Pin.HIGH', True can also work
	print "\n\tThe light is now on. •‿•\n"
	time.sleep(0.5)

def turnOFF(color):
	"Turns off lights"
	Pin.output(color,Pin.LOW)#Instead of 'Pin.LOW', False can also work
	print "\n\t•‿• The light is now off.\n"
	time.sleep(0.5)

#def switch():
#	while True:
#		Do you want to turn on or turn off a light?

def switch():
	print ("Do you want to turn on or turn off a light?")
	while True:
		O = raw_input("""
	1 -> on		2 -> off
		""")
		if O == '1' or O == 'on':
			ask_color('turn on',turnON)




def ask_color(a,b):
	while True:
		ask_col = "\tWhich light do you want to %s ?\n\t\t>" % a
		color = raw_input(ask_col).lower()
		time.sleep(0.5)
		
		if color in color_list:
			b(eval(color))
			break
		
		else:
			print 'sorry'
