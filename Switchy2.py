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
            print ("The " + self.name + " light is on.")
        elif GPIO.input(self.pin) == 0:
            print ("The " + self.name + " light is off.")

    def toggle_switch(self):
        if GPIO.input(self.pin):
            GPIO.output(self.pin,0)
            print ("The " + self.name + " light was turned off.")
        elif GPIO.input(self.pin) == 0:
            GPIO.output(self.pin,1)
            print ("The " + self.name + " light was turned on.")

L1 = lights("white", 21)
L2 = lights("yellow", 16)
L3 = lights("red", 12)
L4 = lights("blue", 25)
L5 = lights("green", 24)
L6 = lights("snow", 13)

try:
    for i in [L1,L2,L3,L4,L5,L6]:
        time.sleep(0.5)
        i.toggle_switch()
            
    print ("yep. The switch works fine!\n")
    time.sleep(1)

    while True:
        ask_color = raw_input("\tWhich light?\n\t\t>");
        color = ask_color.lower()
        time.sleep(0.5)

        if color == L1.name:
            L1.toggle_switch()

        elif color == L2.name:
            L2.toggle_switch()

        elif color == L3.name:
            L3.toggle_switch()
            
        elif color == L4.name:
            L4.toggle_switch()

        elif color == L5.name:
            L5.toggle_switch()

        elif color == L6.name:
            L6.toggle_switch()

        elif color == 'none' or color == '':
            break

        else:
            print("""
✖﹏✖
✖﹏✖ Sorry but this color is not available. ✖﹏✖
✖﹏✖

""")
            time.sleep(0.5)

    GPIO.cleanup()

except KeyboardInterrupt:
    GPIO.cleanup()
