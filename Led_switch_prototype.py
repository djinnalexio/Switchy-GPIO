import RPi.GPIO as Pin
import time
Pin.setmode(Pin.BCM)
Pin.setwarnings(False)

white2=18
White2=18
green=24
Green=24
blue=8
Blue=8
red=12
Red=12
yellow=16
Yellow=16
white=21
White=21
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

name = raw_input( """
	Hello. First, let's introduce ourselves. I'm Switch and my job is to
	control the lights plugged on the breadboard. And you, what's your name?
				->""")

print ("""
	Hi %s! Nice to meet you! As I just said, I am an application
	that allows you to control the lights next to you. I can turn them on,
	turn them off, and even make them blink for as long as you want.

				All you have to do is type.""") % name

while True:
	action = raw_input("""
	To turn on a light(s), type 'on'	To turn off a light(s), type 'off'
	
	To make a light(s) blink, type 'blink'		To exit, type 'none'
	
		To learn about the colors at your disposal, type 'color'
		
		>""")
		
	if action == "color":
			print("""
	The colors are white, yellow, red, blue, green, and white2
	
		To control several colors at once, use comas.
	
	Ex: Which led do you want to turn on?
			>white, red
	""")
	
	if action == "on":
		color = input("\tWhich led do you want to turn on?\n\t\t>")
		if color == none:
			break
		turnON(color)
	
	if action == "off":
		color = input("\tWhich led do you want to turn off?\n\t\t>")
		if color == none:
			break
		turnOFF(color)
		
	if action == "blink":
		color = input("\tWhich led do you want to blink?\n\t\t>")
		if color == "none":
			break
		ask_blink_time = raw_input("\tFor how long do you want the light to blink?(in seconds)\n\t\t>")
		if ask_blink_time == none:
			break
		blink_time = int(ask_blink_time)
		blink(color, blink_time)
		
	if action == "none":
		break

print "\n\tYou exit the switch. See you next time %s!" % name
