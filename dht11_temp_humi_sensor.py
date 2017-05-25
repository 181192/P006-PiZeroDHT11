#!/usr/bin/python
import sys, curses, time
import Adafruit_DHT

scr = curses.initscr()


while True:
	humidity, temperature = Adafruit_DHT.read_retry(11, 4)

	scr.addstr(0, 0, 'Temp: {0:0.1f} C Humidity: {1:0.1f} %'.format(temperature, humidity))
	scr.refresh()
	time.sleep(1)

