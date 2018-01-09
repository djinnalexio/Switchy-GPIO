#!/usr/bin/python
# -*- coding: utf-8 -*-

#By Andre Akue

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)

class lights:

    def __init__(self,color_name,color_pin):
	    self.name = color_name
		self.pin = color_pin
	
	GPIO.setup(self.pin, GPIO.OUT)
	
	def check_state(self):
	    if GPIO.input(self.pin):
		    print ("The " + self.color_name + "light is on.")
		elif GPIO.input(self.pin) == 0:
		    print ("The " + self.color_name + "light is off.")
	
	def toggle_switch(self):
	    if GPIO.input(self.pin):
		    GPIO.output(self.pin,0)
			print ("The " + self.color_name + " was turned off.")
		elif GPIO.input(self.pin) == 0:
		    GPIO.output(self.pin,1)
			print ("The " + self.color_name + " was turned on.")

L1 = lights(L1, "white", 21)
L2 = lights(L2, "yellow", 16)
L3 = lights(L3, "red", 12)
L4 = lights(L4, "blue", 25)
L5 = lights(L5, "green", 24)
L6 = lights(L6, "white", 13)

for i in [L1,L2,L3,L4,L5,L6]:
    time.sleep(1)
	i.check_state()