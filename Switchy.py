#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as Pin
import time
Pin.setmode(Pin.BCM)
Pin.setwarnings(False)

#grounds = 6, 9, 14, 20, 25, 30, 34, 39

blue=25 #22
Pin.setup(blue, Pin.OUT)
green=24 #18
Pin.setup(green, Pin.OUT)
red=12 #32
Pin.setup(red, Pin.OUT)
white=21 #40
Pin.setup(white, Pin.OUT)
white2=17 #11
Pin.setup(white2, Pin.OUT)
yellow=16 #36
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
	"Pattern 2: 2 moving lights"

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
	"Pattern 3: moving shadow"

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
	"Pattern 4: 2 moving shadows"

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


help_answer = """
		When you are in a menu, choose an option by typing the
		number in front of it and pressing RETURN(ENTER).
		
		When I ask you questions, please enter only values or
		or terms I can use. For example, when I ask for a color,
		you should only type one of the available ones.
		
		If I ask for a value (such as the duration and speed),
		please only use digits or else I won't understand.
		
		To return to the main menu, answer a question with 'none'.
		
		"""

help_main_menu = """
		When in the MAIN MENU, select an action
			by typing its number:
			
		1	You can turn on a light or all the lights at once.
			!!It doesn't have any effect if the light is already on.
		
		2	You can turn off a light or all the lights at once.
			!!It doesn't have any effect if the light is already off.
		
		3	You can make a light blink or make all the lights
					blink together.
			!!While a light is blinking, NOTHING ELSE can be done until
				the end of the entered duration. Thus, you will have to
				wait for this long before doing anything else!
			!!After blinking, the light(s) will always end up off
				regardless of the starting state.
			!!While the lights are blinking, I will displayed the
						elasped time.
			
		4	You can watch light shows! You can even control the 
				duration and the speed of the selected light show!
			!!Just like with the option '3', you CAN'T DO ANYTHING
				during the light show
			!!To assure a smooth start, lights will be automatically
				turned off before starting the light show.
			
		5	You can ask me to show you these instructions again.
		
		6	You can leave anytime you want from here. 
		
		7	You can type feedback. I will use your impressions and 
				suggestions to get even better!
		
		"""

help_color = """
		The colors are(from right to left):
		
		white	
			green
		blue
			red
		yellow
			white2
		
		To select all the lights at the same time, type 'All of them'.
		
		Type 'none' if you want to go back to the main menu.
				"""

				
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
		
		raw_input()
		
		#first time explanation
		
		print("""
	•‿• ^‿^ •‿• ^‿^ •‿• ^‿^ •‿• ^‿^ •‿• ^‿^ •‿• ^‿^ •‿•
	
		It's time to see how things work^‿^""")
		
		raw_input()
		
		print help_answer
		
		raw_input()
		
		print help_main_menu
		
		raw_input()
		
		print help_color
		
		raw_input()
		
		print("""
		We're done with the introduction and the explanation.
		Now, enjoy!
		
		•‿• ^‿^ •‿• ^‿^ •‿• ^‿^ •‿• ^‿^ •‿• ^‿^ •‿• ^‿^ •‿•
		
		""")
		
		time.sleep(1)
		
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
						5:Ask for HELP
	2:Turn OFF lights
							6:STOP Switchy
3:Make lights BLINK
						7:Give FEEDBACK
	4:Start LIGHT SHOWS
						
		^‿^ So, what do you want to do?""")
	action = raw_input("""			Type a number here ->""")
			
	print '\n_______________________________________________________\n'
	time.sleep(0.5)
		
	if action == '1':#Turn ON
		while True:
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

			elif color == 'none' or color == '':
				break

			else:
				print("""
				✖﹏✖
		✖﹏✖ Sorry but this color is not available. ✖﹏✖
				✖﹏✖

	""")
				time.sleep(0.5)
			
	elif action == '2':#Turn OFF
		while True:
			ask_color = raw_input("\tWhich light do you want to turn OFF?\n\t\t>");
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

			elif color == 'none' or color == '':
				break

			else:
				print("""
				✖﹏✖
		✖﹏✖ Sorry but this color is not available. ✖﹏✖
				✖﹏✖

	""")
				time.sleep(0.5)
			
	elif action == '3':#BLINK
		while True:
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

			elif color == 'none' or color == '':
				break

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
		time.sleep(1)
		
		while True:
			print("""
	Here are the available light shows:

1:Moving Light

2:Moving Light 2
									0:Back to main menu
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






			elif l_s == 'none' or l_s == '':#exit light shows
				break

			else:#not defined
				time.sleep(1)
				print("""
				✖﹏✖
		✖﹏✖ Sorry. I didn't understand what you typed. ✖﹏✖
				✖﹏✖

	""")
				time.sleep(1)
		
	elif action == '5':#HELP
		while True:
			print("""
		^‿^ So, what do you need help with?

1:Ansewring Questions

2:Main Menu							0:Back to main menu

3:Colors
			""")
			
			ask_h = raw_input("""			Type a number here ->""")
			
			time.sleep(1)

			if ask_h == '1':#help with Ansewring Questions
				print help_answer
				
			elif ask_h == '2':#help with main menu
				print help_main_menu
				
			elif ask_h == '3':#help with colors
				print help_color
				
			elif ask_h == '4':#back to main menu
				break
				
			else:#not defined
				print("""
				✖﹏✖
		✖﹏✖ Sorry. Can you repeat?. ✖﹏✖
				✖﹏✖

	""")
				time.sleep(0.5)

	elif action == '6':#STOP
		print ("\tAlright %s. See you next time! ^‿^\n") % username
		print("""
☻ ☼ ☽ ☾ ♠ ♡ ♢ ♣ ♤ ♥ ♦ ♧ ♨ ♩ ✙ ✈ ✉ ✌ ✁ ✎ ✐ ❀ ✰ ❁ ☻ ☼ ☽ ☾ ♠ ♡ ♢ ♣ ♤ ♥ ♦ ♧ 
""")
		break

	elif action == '7':#Suggestions
		feedback = open('Switchy_suggestions.txt','a+')
		
		print("""
		•‿• Alright! Here, I'll let you write what you think of me,
			and how you would like me to change to improve myself •‿•
		 """)
		 		
		suggestion = raw_input("\t\tFeedback:\n\t>")
		
		new_suggestion = "%s\n\n" % suggestion
		
		feedback.write(new_suggestion)
		
		feedback.close()
		
		time.sleep(0.5)
		
		print("""
		
		•‿•Thank you for your opinion!•‿•
		""")
	
	else:#not defined
		time.sleep(1)
		print("""
				✖﹏✖
		✖﹏✖ Sorry but I didn't get it... ✖﹏✖
				✖﹏✖

	""")
		time.sleep(0.5)
