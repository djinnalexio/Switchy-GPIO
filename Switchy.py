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
color_names = ('blue', 'green', 'red', 'white', 'white2', 'yellow')

def turnON(color):
	"Turns on lights"
	Pin.output(color,Pin.HIGH)
	print "\n\tThe light is now on. •‿•\n"
	time.sleep(1.5)

def turnOFF(color):
	"Turns off lights"
	Pin.output(color,Pin.LOW)
	print "\n\t•‿• The light is now off.\n"
	time.sleep(1.5)

def blink(color):
	"Makes lights blink for <duration> seconds"
	
	duration = int(raw_input("\tFor how long do you want the light to blink? (in seconds)\n\t\t>"))
	blink_speed = float(raw_input("\n\tChoose a blinking speed •‿•\n\t\t>"))
	blink_inter = 0.5 / blink_speed
	print "\n\tThe light will be blinking for %i seconds.\nSpeed: %d." % (duration, blink_speed)
	print "		•‿•Starting in:"
	time.sleep(1)
	for i in range(0,3):
		print "\t\t\t",3 - i
		time.sleep(1)
	count = range(0,duration)
	for i in count:
		print i + 1
		Pin.output(color,Pin.HIGH)
		time.sleep(blink_inter)
		Pin.output(color,Pin.LOW)
		time.sleep(blink_inter)
		Pin.output(color,Pin.HIGH)
		time.sleep(blink_inter)
		Pin.output(color,Pin.LOW)
		time.sleep(blink_inter)
		Pin.output(color,Pin.HIGH)
		time.sleep(blink_inter)
		Pin.output(color,Pin.LOW)
		time.sleep(blink_inter)
	print "\n\tWell, 'looks like that's it! anything else?!^‿^\n"
	time.sleep(1.5)

#def passing_shadow(duration):

#def alt_blink(duration):

#def countdown(duration):

skip_intro = raw_input("Do you want to skip the introduction?(Y/N)")
s_i = skip_intro.lower()

if s_i == '' or s_i == 'n' or s_i == 'no':
#asking for name
	print ("""
☻ ☼ ☽ ☾ ♠ ♡ ♢ ♣ ♤ ♥ ♦ ♧ ♨ ♩ ✙ ✈ ✉ ✌ ✁ ✎ ✐ ❀ ✰ ❁ ☻ ☼ ☽ ☾ ♠ ♡ ♢ ♣ ♤ ♥ ♦ ♧ 

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

#presentation of the app
	print("""
☻ ☼ ☽ ☾ ♠ ♡ ♢ ♣ ♤ ♥ ♦ ♧ ♨ ♩ ✙ ✈ ✉ ✌ ✁ ✎ ✐ ❀ ✰ ❁ ☻ ☼ ☽ ☾ ♠ ♡ ♢ ♣ ♤ ♥ ♦ ♧ 

		So your name is %s. Ok!•‿•""") % username


#first time explanation





#app main menu: on, off, blink, light shows, help, (leave)
while True:
	
	choice_action = ('1','2','3','4','5','6')
	
	ask_action = raw_input("""
☻ ☼ ☽ ☾ ♠ ♡ ♢ ♣ ♤ ♥ ♦ ♧ ♨ ♩ ✙ ✈ ✉ ✌ ✁ ✎ ✐ ❀ ✰ ❁ ☻ ☼ ☽ ☾ ♠ ♡ ♢ ♣ ♤ ♥ ♦ ♧ 
				♦MAIN MENU♦


1:Turn ON lights
						4:Start LIGHT SHOWS
	2:Turn OFF lights
							5:Ask for HELP
3:Make lights BLINK
						6:STOP Switchy
	
		^‿^ So, what do you want to do?
			Type a number here ->""")
			
	print '\n'

	if ask_action not in choice_action:
		time.sleep(2)
		print("""
				✖﹏✖
		✖﹏✖ Sorry but I didn't get it... ✖﹏✖
				✖﹏✖

	""")
		time.sleep(1)
		
	time.sleep(1)
	
	if ask_action == '1':#Turn ON
		time.sleep(1)
		ask_color = raw_input("\tWhich light do you want to turn ON?\n\t\t>");
		color = ask_color.lower()
		time.sleep(1)

		if color == 'blue':
			turnON(blue)
			
		if color == 'green':
			turnON(green)
			
		if color == 'red':
			turnON(red)			
		
		if color == 'white':
			turnON(white)
			
		if color == 'white2':
			turnON(white2)			
			
		if color == 'yellow':
			turnON(yellow)

		if color not in color_names:
			print("""
				✖﹏✖
		✖﹏✖ Sorry but this color is not available. ✖﹏✖
				✖﹏✖

	""")
			time.sleep(1)
			
	if ask_action == '2':#Turn OFF
		time.sleep(1)
		ask_color = raw_input("\tWhich led do you want to turn OFF?\n\t\t>")
		color = ask_color.lower()
		time.sleep(1)

		if color == 'blue':
			turnOFF(blue)
			
		if color == 'green':
			turnOFF(green)
			
		if color == 'red':
			turnOFF(red)			
		
		if color == 'white':
			turnOFF(white)
			
		if color == 'white2':
			turnOFF(white2)			
			
		if color == 'yellow':
			turnOFF(yellow)

		if color not in color_names:
			print("""
				✖﹏✖
		✖﹏✖ Sorry but this color is not available. ✖﹏✖
				✖﹏✖

	""")
			time.sleep(1)

	if ask_action == '3':#BLINK
		time.sleep(1)
		ask_color = raw_input("\tWhich led do you want to blink?\n\t\t>")
		color = ask_color.lower()
		time.sleep(1)

		if color == 'blue':
			blink(blue)
			
		if color == 'green':
			blink(green)
			
		if color == 'red':
			blink(red)			
		
		if color == 'white':
			blink(white)
			
		if color == 'white2':
			blink(white2)			
			
		if color == 'yellow':
			blink(yellow)

		if color not in color_names:
			print("""
				✖﹏✖
		✖﹏✖ Sorry but this color is not available. ✖﹏✖
				✖﹏✖

	""")
			time.sleep(1)
