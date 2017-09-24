#!/usr/bin/python
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)  # Using pin numbers

# Setting up pins
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


#GPIO.setup(24, GPIO.OUT)

#Get Pin Input
inputValue = GPIO.input(17)
#print (inputValue)
intValue= str(inputValue)
'''
f = open('/var/www/html/relay-status.txt','w')
f.write(intValue)
f.close()'''

if GPIO.input(17)== False:
    
    print ("Door is open")
else:
    print ("Door is closed")

GPIO.cleanup () 
