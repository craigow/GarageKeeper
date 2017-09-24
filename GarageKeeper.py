#!/usr/bin/python

import RPi.GPIO as GPIO
import smtplib
import time
#Garage door monitor with SMS warning

forever = (1)
sleep = 300
#Pin Definitions

switchPin = 17
relayPin = 24


#Set up GPIO
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)  # Using pin numbers
GPIO.setup(switchPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)



CurrentTime=time.strftime('%H') # Get current time in hours only
TimeInt = int(CurrentTime) 
t = time.localtime()

#Get Status
inputValue = GPIO.input(17)
intValue= str(inputValue)

try:
   while forever == 1:
      while GPIO.input(switchPin)== False:
         CurrentTime=time.strftime('%H') # Get current time in hours only
         TimeInt = int(CurrentTime) 
         print (TimeInt)
         if (TimeInt <=8) or (TimeInt >=21):
            GPIO.cleanup(relayPin)
            GPIO.setup(relayPin, GPIO.OUT, initial=GPIO.LOW)
            GPIO.output(relayPin, 1)
            time.sleep(0.5)
            GPIO.cleanup(relayPin)
            print ("Garage Open")
	    f = open('/var/www/html/relay-status.txt','w')
	    f.write(intValue)
            f.close()

            t = time.localtime()
            print (time.asctime(t))
            server = smtplib.SMTP( "smtp.gmail.com", 587 )
            server.starttls()
            server.login('email', 'password')
            server.sendmail('GarageKeeper', 'cell@tmobile.net', 'Subject: Door Open.  Close signal sent!' )
            server.quit()
            print  ("Close door request sent. Text sent! Checking again in 5 minutes")

            time.sleep (sleep) #wait 10 minutes and repeat process
         else:
            print('Daytime. Door Open.')
            t = time.localtime()
            print (time.asctime(t))

 	    f = open('/var/www/html/relay-status.txt','w')
       	    f.write(intValue)
	    f.close()

            time.sleep (sleep) #wait 10 minutes and repeat process


      while GPIO.input(switchPin)== True:
         print ("Door Closed")

	 f = open('/var/www/html/relay-status.txt','w')
	 f.write(intValue)
         f.close()

         t = time.localtime()
         print (time.asctime(t))
         time.sleep(sleep)

   #time.sleep (600) #wait 10 minutes and repeat process
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO