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
color_names = ('blue', 'green', 'red', 'white', 'white2', 'yellow', 'all', 'all of them')

print("""
	Hi there! So you're interested in light shows?•‿•
			
			Alright! Let's have fun! ^‿^
""")

raw_input()

print("""
	Here are the available light shows:

1:Moving Light
						2:Moving Light 2
3:Alternated Blink
						4:Alternated Blink by 2
5:Alternated Blink by 3
						6:Countdown
7:Priority Vehicule Lights						
						8:coming soon
						
		^‿^ So, what do you want to do?
			""")
			
l_s = raw_input("""			Type a number here ->""")
		
if l_s == '1':#Moving Light
			
elif l_s == '2':#Moving Light 2
			
elif l_s == '3':#Alternated Blink
			
elif l_s == '4':#Alternated Blink by 2
			
elif l_s == '5':#Alternated Blink by 3
			
elif l_s == '6':#Countdown
			
elif l_s == '7':#Priority Vehicule Lights
			
elif l_s == '8':#coming soon
			
else:#not defined
