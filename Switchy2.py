#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import time
import RPi.GPIO as Pin
Pin.setmode(Pin.BCM)
Pin.setwarnings(True)

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
white= (left, right)
all = (left, yellow, red, blue, green, right)

color_list = ['all', 'left', 'yellow', 'red', 'blue', 'green', 'right', 'white']
led_list = [left, yellow, red, blue, green, right]

def switch():
	print ("Do you want to turn on or turn off a light?")
	while True:
		O = raw_input("""
1 -> on	2 -> off	3 -> Check status

0 -> back to main menu
		""")
		if O == '1' or O.lower() == 'on':
			ask_color('turn on',turnON)
		elif O == '2' or O.lower() == 'off':
			ask_color('turn off',turnOFF)
		elif O == '3':
			ask_color('check',check)
		elif O == '0':
			break
		else:
			print ("Please try again")

def ask_color(a,b):
	while True:
		ask_col = "Which light do you want to %s?\n\t>" % a
		color = raw_input(ask_col).lower()
		time.sleep(0.5)
		
		if color in color_list:
			b(eval(color),color)
			return
		
		else:
			print 'sorry'
			return

def check(color,color_name):
	try:
		if Pin.input(color) == True:#only works with one integer
			print '\n%s is on' % color_name
		else:
			print '\n%s is off' % color_name
	except:
		print '\ncan\'t check this color'

def turnON(color,color_name):
	"Turns on lights"
	Pin.output(color,Pin.HIGH)#Instead of 'Pin.HIGH', True can also work
	if color_name == 'all':
		print "\nAll the lights are now on. •‿•\n"
	else:
		print "\nThe %s light is now on. •‿•\n" % color_name
	time.sleep(0.5)

def turnOFF(color,color_name):
	"Turns off lights"
	Pin.output(color,Pin.LOW)#Instead of 'Pin.LOW', False can also work
	if color_name == 'all':
		print "\nAll the lights are now off. •‿•\n"
	else:
		print "\nThe %s light is now off. •‿•\n" % color_name
	time.sleep(0.5)

def blink(color,color_name):
	"Makes lights blink for <duration> seconds"

	if color_name == 'all':
		ask_d = "\nFor how long do you want the lights to blink? (in seconds)\n\t\t>"
	else:
		ask_d = "\nFor how long do you want the %s light to blink? (in seconds)\n\t\t>" % color_name
	ask_duration = raw_input(ask_d)
	if ask_duration.isdigit():
		duration = int(ask_duration)
	else:
		print ("sorry")
		time.sleep(1)
		return
	
	ask_blink_speed = raw_input("\nChoose a blinking speed •‿•\n\t\t>")
	if ask_blink_speed.isdigit() :
		inter = 0.5 / int(ask_blink_speed)
	else:
		print ("sorry")
		time.sleep(1)
		return
	
	stp = time.time() ; etp = time.time() + duration# stp/etp = starting / ending time pattern
	while time.time() < etp: 
		print (int(time.time() - stp))# elased time = current time - time start blink
		Pin.output(color,True)
		time.sleep(inter)
		Pin.output(color,False)
		time.sleep(inter)
			
	print "\ndone\n"
	time.sleep(0.5)

def ask_time():
	duration = raw_input("\nFor how long do you want the pattern to run for? (in seconds)\n\t>")
	if duration.isdigit():
		duration = int(duration)
	else:
		return
	
	print "\n\tThe light show will run for about %s seconds." % duration
	time.sleep(1)
	return duration

def ask_time_and_speed():
	duration = raw_input("\nFor how long do you want the pattern to run for? (in seconds)\n\t>")
	if duration.isdigit():
		duration = int(duration)
	else:
		return
	
	speed = raw_input("\nChoose a speed for the lights•‿•\n\t>")
	if speed.isdigit() :
		inter = 0.5/int(speed)
	else:
		return
	
	print "\n\tThe light show will run for about %s seconds.\n\tSpeed: %s." % (duration, speed)
	time.sleep(1)
	return duration, inter

def light_shows():
	print "Here are light shows"
	time.sleep(1)
	while True:
		print("""
1:Moving Light	2:Moving Shadow	3:Police Car

4:Back and Forth	5:Two by Two	6:Random

0:Back to main menu
""")

		l_s = raw_input("""			Type a number here ->""")

		if l_s == '1':#Moving Light
			try:
				duration, inter = ask_time_and_speed()
			except TypeError:
				print 'not number'
				break
			moving_light(duration,inter)
			time.sleep(0.5)

		elif l_s == '2':#Moving Shadow
			try:
				duration, inter = ask_time_and_speed()
			except TypeError:
				print 'not number'
				break
			moving_shadow(duration,inter)
			time.sleep(0.5)

		elif l_s == '3':#police car
			try:
				duration = ask_time()
			except TypeError:
				print 'not number'
				break
			police_car(duration)
			time.sleep(0.5)

		elif l_s == '4':#back an'forth
			try:
				duration, inter = ask_time_and_speed()
			except TypeError:
				print 'not number'
				break
			back_an_forth(duration,inter)
			time.sleep(0.5)

		elif l_s == '5':#two by two
			try:
				duration, inter = ask_time_and_speed()
			except TypeError:
				print 'not number'
				break
			two_by_two(duration,inter)
			time.sleep(0.5)

		elif l_s == '6':#Random
			try:
				duration, inter = ask_time_and_speed()
			except TypeError:
				print 'not number'
				break
			rm(duration,inter)
			time.sleep(0.5)

		elif l_s == '0':#exit light shows
			break

		else:#not defined
			time.sleep(1)
			print("""not defined""")
			time.sleep(1)

def moving_light(duration,inter):
	Pin.output(all,False)
	print ('code is running')
	etp = time.time() + duration # etp = ending time pattern
	while time.time() <= etp:		
		for i in led_list:
			Pin.output(i,True)
			time.sleep(inter)
			Pin.output(i,False)

def moving_shadow(duration,inter):
	Pin.output(all,True)
	print ('code is running')
	etp = time.time() + duration # etp = ending time pattern
	while time.time() <= etp:		
		for i in led_list:
			Pin.output(i,False)
			time.sleep(inter)
			Pin.output(i,True)
	Pin.output(all,False)
	
def police_car(duration):
	led_list = [blue,red]
	Pin.output(all,False)
	time.sleep(.75)
	Pin.output(white,True)
	time.sleep(.5)
	print ('code is running')
	etp = time.time() + duration # etp = ending time pattern
	while time.time() <= etp:		
		for i in led_list:
			Pin.output(i,True)
			time.sleep(.2)
			Pin.output(i,False)
	Pin.output(all,False)

def back_an_forth(duration,inter):
	l1 = (red,blue)
	l2 = (yellow,green)
	light_list = [l1,l2]
	Pin.output(all,False)
	time.sleep(.75)
	Pin.output(white,True)
	time.sleep(.5)
	print ('code is running')
	etp = time.time() + duration # etp = ending time pattern
	while time.time() <= etp:		
		for i in light_list:
			Pin.output(i,True)
			time.sleep(inter)
			Pin.output(i,False)
	Pin.output(all,False)

def two_by_two(duration,inter):
	l1 = (left,yellow)
	l2 = (red,blue)
	l3 = (green,right)
	light_list = [l1,l2,l3]
	Pin.output(all,False)
	print ('code is running')
	etp = time.time() + duration # etp = ending time pattern
	while time.time() <= etp:		
		for i in light_list:
			Pin.output(i,True)
			time.sleep(inter)
			Pin.output(i,False)

def rm(duration,inter):
	Pin.output(all,False)
	print ('code is running')
	etp = time.time() + duration # etp = ending time pattern
	while time.time() <= etp:		
		for i in led_list:
			j = random.choice(led_list)
			Pin.output(j,True)
			time.sleep(inter)
			Pin.output(j,False)
			time.sleep(inter)

while True:
	print("""
1 -> Light Switch		2 -> Blink

3 -> Light Shows
	""")
	action = raw_input("""			 ->""")
	if action == '1':
		switch()
		
	elif action == '2':
		ask_color('blink',blink)
	
	elif action == '3':
		light_shows()
		
	else:
		print 'not defined'
		break	

Pin.output(all,Pin.LOW)
Pin.cleanup()