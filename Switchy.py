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

def blink(color):
	"Makes lights blink for <duration> seconds"

	ask_duration = raw_input("\n\tFor how long do you want the light(s) to blink? (in seconds)\n\t\t>")
	if ask_duration.isdigit():
		duration = int(ask_duration)
	else:
		print ("""
				✖﹏✖
		✖﹏✖ Sorry, I didn't get what you meant... ✖﹏✖
				✖﹏✖

	""")
		time.sleep(1)
		return
	
	ask_blink_speed = raw_input("\n\tChoose a blinking speed •‿•\n\t\t>")
	if ask_blink_speed.isdigit() :
		blink_inter = 0.5 / int(ask_blink_speed)
	else:
		print ("""
				✖﹏✖
		✖﹏✖ Sorry, I didn't get what you meant... ✖﹏✖
				✖﹏✖

	""")
		time.sleep(1)
		return
	
	print "\n\tThe light(s) will be blinking for %s seconds.\n\tSpeed: %s blink/sec." % (ask_duration, ask_blink_speed)

	print "		•‿•Starting in:"
	time.sleep(1)
	for i in range(0,3):
		print "\t\t\t",3 - i
		time.sleep(1)

	t_s_b = time.time()#time start blink
	end_blink = time.time() + duration#time end blink
	while time.time() < end_blink:#while current time is small then end time
		print (int(time.time() - t_s_b))# count blink = current time - time start blink
		Pin.output(color,Pin.HIGH)
		time.sleep(blink_inter)
		Pin.output(color,Pin.LOW)
		time.sleep(blink_inter)


	print "\n\tWell, 'looks like that's it! anything else?!^‿^\n"
	time.sleep(0.5)


def moving_light():
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

	print "		•‿•Starting in:"
	time.sleep(1)	
	for i in range(0,3):
		print "\t\t\t",3 - i
		time.sleep(1)

	stp = time.time() ; etp = time.time() + duration# stp/etp = starting / ending time pattern
	while time.time() < etp: 
		print (int(time.time() - stp))# elased time = current time - time start blink
		Pin.output(white2,True)
		
		time.sleep(inter)
		Pin.output(white2,False)
		Pin.output(green,True)
		
		time.sleep(inter)
		Pin.output(green,False)
		Pin.output(blue,True)
		
		time.sleep(inter)
		Pin.output(blue,False)
		Pin.output(red,True)
		
		time.sleep(inter)
		Pin.output(red,False)
		Pin.output(yellow,True)
		
		time.sleep(inter)
		Pin.output(yellow,False)
		Pin.output(white,True)
		
		time.sleep(inter)
		Pin.output(white,False)

def moving_light2():
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

	print "		•‿•Starting in:"
	time.sleep(1)	
	for i in range(0,3):
		print "\t\t\t",3 - i
		time.sleep(1)

	stp = time.time() ; etp = time.time() + duration# stp/etp = starting / ending time pattern
	while time.time() < etp: 
		print (int(time.time() - stp))# elased time = current time - time start blink
		Pin.output(white2,True)
		
		time.sleep(inter)
		Pin.output(white,False)
		Pin.output(green,True)
		
		time.sleep(inter)
		Pin.output(white2,False)
		Pin.output(blue,True)
		
		time.sleep(inter)
		Pin.output(green,False)
		Pin.output(red,True)
		
		time.sleep(inter)
		Pin.output(blue,False)
		Pin.output(yellow,True)
		
		time.sleep(inter)
		Pin.output(red,False)
		Pin.output(white,True)
		
		time.sleep(inter)
		Pin.output(yellow,False)
	
	time.sleep(inter)	
	Pin.output(white,False)
	
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


while True:#Skip Intro?
	skip_intro = raw_input("Do you want to skip the introduction? 'Y' or 'N' >")
	s_i = skip_intro.lower()

	if s_i == 'n':
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

		print("""
☻ ☼ ☽ ☾ ♠ ♡ ♢ ♣ ♤ ♥ ♦ ♧ ♨ ♩ ✙ ✈ ✉ ✌ ✁ ✎ ✐ ❀ ✰ ❁ ☻ ☼ ☽ ☾ ♠ ♡ ♢ ♣ ♤ ♥ ♦ ♧ 

		So your name is %s. Ok!•‿•"""
		) % username
		
		#first time explanation
		
		
		
		break
		
	elif s_i == 'y':
		username = raw_input("\nname: ")
		break
		
	else:
		print ("\n<Please answer with Y for 'Yes' or N for 'No'>\n")

while True:#app main menu: on, off, blink, light shows, help, (leave)
		
	print("""
☻ ☼ ☽ ☾ ♠ ♡ ♢ ♣ ♤ ♥ ♦ ♧ ♨ ♩ ✙ ✈ ✉ ✌ ✁ ✎ ✐ ❀ ✰ ❁ ☻ ☼ ☽ ☾ ♠ ♡ ♢ ♣ ♤ ♥ ♦ ♧ 
				♦MAIN MENU♦


1:Turn ON lights
						4:Start LIGHT SHOWS
	2:Turn OFF lights
							5:Ask for HELP
3:Make lights BLINK
						6:STOP Switchy
	
		^‿^ So, what do you want to do?""")
	action = raw_input("""			Type a number here ->""")
			
	print '\n_______________________________________________________\n'
	time.sleep(0.5)
		
	if action == '1':#Turn ON
		ask_color = raw_input("\tWhich light do you want to turn ON?\n\t\t>");
		color = ask_color.lower()
		time.sleep(0.5)

		if color == 'all' or color == 'all of them':
			Pin.output(colors,Pin.HIGH)
			print "\n\tAll the lights are now on. •‿•\n"
			time.sleep(0.5)

		elif color == 'blue':
			turnON(blue)
			
		elif color == 'green':
			turnON(green)
			
		elif color == 'red':
			turnON(red)			
		
		elif color == 'white':
			turnON(white)
			
		elif color == 'white2':
			turnON(white2)			
			
		elif color == 'yellow':
			turnON(yellow)

		else:
			print("""
				✖﹏✖
		✖﹏✖ Sorry but this color is not available. ✖﹏✖
				✖﹏✖

	""")
			time.sleep(0.5)
			
	elif action == '2':#Turn OFF
		ask_color = raw_input("\tWhich led do you want to turn OFF?\n\t\t>")
		color = ask_color.lower()
		time.sleep(0.5)

		if color == 'all' or color == 'all of them':
			Pin.output(colors,Pin.LOW)
			print "\n\tAll the lights are now off. •‿•\n"
			time.sleep(0.5)

		elif color == 'blue':
			turnOFF(blue)
			
		elif color == 'green':
			turnOFF(green)
			
		elif color == 'red':
			turnOFF(red)			
		
		elif color == 'white':
			turnOFF(white)
			
		elif color == 'white2':
			turnOFF(white2)			
			
		elif color == 'yellow':
			turnOFF(yellow)

		else:
			print("""
				✖﹏✖
		✖﹏✖ Sorry but this color is not available. ✖﹏✖
				✖﹏✖

	""")
			time.sleep(0.5)

	elif action == '3':#BLINK
		ask_color = raw_input("\tWhich led do you want to blink?\n\t\t>")
		color = ask_color.lower()
		time.sleep(0.5)

		if color == 'all' or color == 'all of them':
			blink(colors)

		elif color == 'blue':
			blink(blue)
			
		elif color == 'green':
			blink(green)
			
		elif color == 'red':
			blink(red)			
		
		elif color == 'white':
			blink(white)
			
		elif color == 'white2':
			blink(white2)			
			
		elif color == 'yellow':
			blink(yellow)

		else:
			print("""
				✖﹏✖
		✖﹏✖ Sorry but this color is not available. ✖﹏✖
				✖﹏✖

	""")
			time.sleep(0.5)

	elif action == '4':#LIGHT SHOWS
		print("""
	Hi there! So you're interested in light shows?•‿•
			
			Alright! Let's have fun! ^‿^
""")

		raw_input()

		print("""
	Here are the available light shows:

1:Moving Light

2:Moving Light 2

3:Moving Shadow

4:Moving Shadow 2

		^‿^ So, what do you want to do?
			""")
			
		l_s = raw_input("""			Type a number here ->""")

		if l_s == '1':#Moving Light
			moving_light()
			time.sleep(0.5)

		elif l_s == '2':#Moving Light 2
			moving_light2()
			time.sleep(0.5)

		elif l_s == '3':#Moving Shadow
			moving_shadow()
			time.sleep(0.5)

		elif l_s == '4':#Moving Shadow 2
			moving_shadow2()
			time.sleep(0.5)

		else:#not defined
			time.sleep(1)
			print("""
				✖﹏✖
		✖﹏✖ Sorry. I didn't understand what you typed. ✖﹏✖
				✖﹏✖

	""")
			time.sleep(1)
		
	elif action == '5':#HELP
		print 'Sorry but this option is not available yet'

	elif action == '6':#STOP
		print ("\tAlright %s. See you next time! ^‿^\n") % username
		print("""
☻ ☼ ☽ ☾ ♠ ♡ ♢ ♣ ♤ ♥ ♦ ♧ ♨ ♩ ✙ ✈ ✉ ✌ ✁ ✎ ✐ ❀ ✰ ❁ ☻ ☼ ☽ ☾ ♠ ♡ ♢ ♣ ♤ ♥ ♦ ♧ 
""")
		break

	else:#not defined
		time.sleep(1)
		print("""
				✖﹏✖
		✖﹏✖ Sorry but I didn't get it... ✖﹏✖
				✖﹏✖

	""")
		time.sleep(0.5)