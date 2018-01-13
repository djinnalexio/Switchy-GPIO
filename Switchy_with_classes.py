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
        GPIO.setup(self.pin, GPIO.OUT, initial = 1)

    def check_state(self):
        if GPIO.input(self.pin):
            print ("\tThe " + self.name + " light is on.")
        elif GPIO.input(self.pin) == 0:
            print ("\tThe " + self.name + " light is off.")

    def toggle_switch(self):
        if GPIO.input(self.pin):
            GPIO.output(self.pin,0)
            print ("\tThe " + self.name + " light was turned off.")
        elif GPIO.input(self.pin) == 0:
            GPIO.output(self.pin,1)
            print ("\tThe " + self.name + " light was turned on.")

    def check_input_switch(self,color):
        if color == self.name:
            self.toggle_switch()
	else:
            pass

L1 = lights("white", 21)
L2 = lights("yellow", 16)
L3 = lights("red", 12)
L4 = lights("blue", 25)
L5 = lights("green", 24)
L6 = lights("snow", 13)


def switch():
    while True:
        ask_color = raw_input("\n\tWhich light?\n\t\t>")
        color = ask_color.lower()

        for i in [L1,L2,L3,L4,L5,L6]:
           lights.check_input_switch(i,color)

        if color == 'none' or color == '':
            print("see ya\n")
            break

        elif color not in [L1.name,L2.name,L3.name,L4.name,L5.name,L6.name]:
            print("""
✖﹏✖ Sorry but this color is not available. ✖﹏✖
""")
+
try:
    while 1:
	    switch()
	GPIO.cleanup()

except KeyboardInterrupt:
    GPIO.cleanup()