#!/usr/bin/python
import sys
import os
from time import sleep
try: 
	import Adafruit_DHT
except RuntimeError:
	print("Feil ved importering av Adafruit_DHT")

try:
	import urllib2
except RuntimeError:
	print("Feil ved importering av urllib2")
	
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Feil ved importering av RPi.GPIO!  Har du husket å kjøre scriptet som sudo?")



DEBUG = 1
# GPIO pinne som mottar data
DHTpin = 4

# API nøkkel
myAPI = "API nøkkel"

GPIO.setmode(GPIO.BCM)

# Henter sensor data
def getSensorData():
    RHW, TW = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, DHTpin)
   
    # returnerer data
    return (str(RHW), str(TW))
    
# main() funksjonen
def main():
    
	print 'starter...'

	baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI
	print baseURL
    
	try:
		RHW, TW = getSensorData()
		f = urllib2.urlopen(baseURL + 
							"&field1=%s&field2=%s" % (TW, RHW))
		print f.read()
		print TW + " " + RHW
		f.close()
		
	except:
		print 'Avslutter.'

# Kaller main
if __name__ == '__main__':
    main()