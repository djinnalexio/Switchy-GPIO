#!/usr/bin/python
# -*- coding: utf-8 -*-

"By Andre Akue"

import RPi.GPIO as GPIO
import time
from os import system
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)

class lights:

	def __init__(self,color_name,color_pin):
		self.name = color_name
		self.pin = color_pin
		GPIO.setup(self.pin, GPIO.OUT, initial = 1)

	def check_state(self):
		if GPIO.input(self.pin):
			print ("\tThe " + self.name + " light is on.")
		elif GPIO.input(self.pin) == 0:
			print ("\tThe " + self.name + " light is off.")

	def toggle_switch(self,color):
		if color == self.name:
			if GPIO.input(self.pin):
				GPIO.output(self.pin,0)
				print ("\tThe " + self.name + " light was turned off.")
			elif GPIO.input(self.pin) == 0:
				GPIO.output(self.pin,1)
				print ("\tThe " + self.name + " light was turned on.")
		else:
			pass

	def blinking(self,color):
		if color == self.name:
			system('clear')
			stp = time.time() ; etp = time.time() + duration # stp/etp = starting / ending time pattern
			while time.time() < etp:
				print ("\n\n\n\n\n\n\n\tThe " + self.name + " light is blinking.")
				print "\n\n\t\t%i/%i seconds" % (int(time.time() - stp),duration)
				GPIO.output(self.pin,0)
				time.sleep(0.5/speed)
				GPIO.output(self.pin,1)
				time.sleep(0.5/speed)
				system('clear')
		else:
			pass	

class settings:
	def display_settings(self):
		print ("\n\nSpeed of displays: lv{0}\n\nDuration of displays: {1} seconds\n\n\n\n".format(speed,duration))
		raw_input()
		
	def set_speed(self):
		try:
			speed = int(raw_input("choose a speed between 1 and 10\n\t>"))
			if speed <= 10 and speed >=1:
				print "\nDuration changed"
				time.sleep(1)
				return speed
			else:
				print("Sorry. This value is invalid. speed set back to default")
				time.sleep(2)
				return 3
		except ValueError:
			print("Sorry. You entered in invalid input. speed set back to default")
			time.sleep(2)
			return 3

	def set_duration(self):
		try:
			duration = int(raw_input("\n\nchoose a duration for the displays\n\t>"))
			print "\nDuration changed"
			time.sleep(1)
			return duration
		except ValueError:
			print("Sorry. You entered in invalid input. duration set back to default")
			time.sleep(2)
			return 20

class light_shows:
	def moving_light(self):
		for i in [L1,L2,L3,L4,L5,L6]:
			GPIO.output(i.pin,0)
		system('clear')
		stp = time.time() ; etp = time.time() + duration # stp/etp = starting / ending time pattern
		while time.time() < etp:
			print ("\n\n\n\n\n\n\n\tMOVING LIGHT")
			print "\n\n\t\t%i/%i seconds" % (int(time.time() - stp),duration)
			for i in [L1,L2,L3,L4,L5,L6]:
				GPIO.output(i.pin,True)
				time.sleep(0.5/speed)
				GPIO.output(i.pin,False)
				system('clear')

	def moving_shadow(self):
		for i in [L1,L2,L3,L4,L5,L6]:
			GPIO.output(i.pin,1)
		system('clear')
		stp = time.time() ; etp = time.time() + duration # stp/etp = starting / ending time pattern
		while time.time() < etp:
			print ("\n\n\n\n\n\n\n\tMOVING LIGHT")
			print "\n\n\t\t%i/%i seconds" % (int(time.time() - stp),duration)
			for i in [L1,L2,L3,L4,L5,L6]:
				GPIO.output(i.pin,False)
				time.sleep(0.5/speed)
				GPIO.output(i.pin,True)
				system('clear')

	def police_car(self):
		for i in [L1,L2,L3,L4,L5,L6]:
			GPIO.output(i.pin,0)
		system('clear')
		GPIO.output([L1.pin,L6.pin],1)
		stp = time.time() ; etp = time.time() + duration # stp/etp = starting / ending time pattern
		while time.time() < etp:
			print ("\n\n\n\n\n\n\n\tMOVING LIGHT")
			print "\n\n\t\t%i/%i seconds" % (int(time.time() - stp),duration)
			for i in [L3,L4]:
				GPIO.output(i.pin,True)
				time.sleep(0.5/speed)
				GPIO.output(i.pin,False)
				system('clear')

def ask_single_color(function):
    while True:
        ask_color = raw_input("\n\tWhich light?\n\t\t>")
        color = ask_color.lower()

        for i in [L1,L2,L3,L4,L5,L6]:
           function(i,color)

        if color == 'none' or color == '':
            print("see ya\n")
            break

        elif color not in [L1.name,L2.name,L3.name,L4.name,L5.name,L6.name]:
            print("""
✖﹏✖ Sorry but this color is not available. ✖﹏✖
""")

L1 = lights("white", 21)
L2 = lights("yellow", 16)
L3 = lights("red", 12)
L4 = lights("blue", 25)
L5 = lights("green", 24)
L6 = lights("snow", 23)

main_menu = """Controlling single lights

1: Check light status	2: Switch	3: Make it blink


For all lights

4: Lights on	5: Blackout


Light displays

6: Moving light	7: Moving shadow	8: Police Car


Settings

10: Change Speed of displays	11: Change Duration

12: Display current settings



20: Exit Switchy

	>"""

speed = 3
duration = 20

sets = settings()
show = light_shows()

time.sleep(2)

try:
	while True:
		system('clear')
		a = raw_input(main_menu)
		
		if a == "1":
			print '\n'
			for i in [L1,L2,L3,L4,L5,L6]:
			   i.check_state()
			raw_input()
		elif a == "2":
			ask_single_color(lights.toggle_switch)
		elif a == "3":
			ask_single_color(lights.blinking)
		elif a == "4":#Lights on
			for i in [L1,L2,L3,L4,L5,L6]:
			   GPIO.output(i.pin,1)
		elif a == "5":#Blackout
			for i in [L1,L2,L3,L4,L5,L6]:
			   GPIO.output(i.pin,0)
		elif a == "6":
			light_shows.moving_light(show)
		elif a == "7":
			light_shows.moving_shadow(show)
		elif a == "8":
			light_shows.police_car(show)
		elif a == "10":
			speed = settings.set_speed(sets)
		elif a == "11":
			duration = settings.set_duration(sets)
		elif a == "12":
			settings.display_settings(sets)
		elif a == "20":#exit
			print ("bye")
			GPIO.cleanup()
			exit()
		elif a == "":
			pass
		else:
			time.sleep(0.5)
			system('clear')
			print ("\n\n\n\n\nSorry. Invalid input")
			time.sleep(2)

except KeyboardInterrupt:
    system('clear')
    print ("\n\n\texited via keyboard interrupt\n\n")
    GPIO.cleanup()
