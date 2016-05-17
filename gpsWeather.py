# coding:utf-8

import urllib.request
import json
import serial
import re
import types
import time

ser = serial.Serial(

			# add your own port name
			# 自分のUSBポート名を記入する
			port = "/dev/tty.usbserial*",

			baudrate = 9600,
			parity = serial.PARITY_NONE,
			bytesize = serial.EIGHTBITS,
			stopbits = serial.STOPBITS_ONE,
			timeout = None,
			xonxoff = 0,
			rtscts = 0,
			)

while True:
	gpsData = ser.readline().decode('utf-8')

	if re.search(r'RMC', gpsData):

		str = gpsData.split(",")

		if str[3] != "":
			lat_60decimal = float(str[3])
			lng_60decimal = float(str[5])
			lat = int(lat_60decimal/100)+(lat_60decimal/100 - int(lat_60decimal/100))*100/60
			lng = int(lng_60decimal/100)+(lng_60decimal/100 - int(lng_60decimal/100))*100/60
			mode = "json"
			metric = "metric"

			# add your API_KEY in appid. for instance, if your API KEY is abcdefghijklmnopqrstuvwxyz, write like under way
			# appid = "abcdefghijklmnopqrstuvwxyz"
			appid = {"add your API_KEY"}

			url = "http://api.openweathermap.org/data/2.5/weather?lat={a}&lon={b}&mode={c}&units={d}&appid={e}".format(a=lat, b=lng, c=mode, d=metric, e=appid)

			response = urllib.request.urlopen(url).readline()
			weather = json.loads(response.decode('utf-8'))	
			
			print(weather['name'])

			# 現在の天気を表示
			print("weather is :", weather['weather'][0]['main'])
			# 現在の気温を表示
			print("temperature is :", weather['main']['temp'])
			print("")
			time.sleep(1.0)

		else:
			print("no data")

