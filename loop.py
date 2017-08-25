import RPi.GPIO as pin
import time
pin.setmode(pin.BCM)
pin.setwarnings(False)

colors = (21, 24, 25, 17, 16, 12)

pin.setup(colors,pin.OUT)

#colors = [21, 16, 12, 25, 24, 17]
colors = [17, 24, 25, 12, 16, 21]

while True:
    for i in colors:
        pin.output(i,True)
        time.sleep(1)
        pin.output(i,False)
#        time.sleep(1)
        
		for i in leds:
			print (int(time.time() - stp))# elased time = current time - time start blink
			Pin.output(i,True)
			time.sleep(inter)
			Pin.output(i,False)
