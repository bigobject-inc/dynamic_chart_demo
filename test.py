#!/usr/bin/python
import time
import requests
import json
from time import gmtime, strftime, localtime
import sys
import random

def main():
	while(1):

		print_str = ""
		print_str += "{\"channel\":\"/data\","
		print_str += "\"chart1_time\":\"" + strftime("%Y-%m-%d<br>%H:%M:%S", localtime()) + "\","
		print_str += "\"chart1_d1\":" + str(random.randint(0,100)) + ","
		print_str += "\"chart1_d2\":" + str(random.randint(0,100)) + ","
		print_str += "\"chart2_time\":\"" + strftime("%Y-%m-%d<br>%H:%M:%S", localtime()) + "\","
		print_str += "\"chart2_d1\":" + str(random.randint(0,100)) + ","
		print_str += "\"chart2_d2\":" + str(random.randint(0,100)) + ","
		print_str += "\"chart3_time\":\"" + strftime("%Y-%m-%d<br>%H:%M:%S", localtime()) + "\","
		print_str += "\"chart3_d1\":" + str(random.randint(0,100)) + ","
		print_str += "\"chart3_d2\":" + str(random.randint(0,100)) + ","
		print_str += "\"chart4_time\":\"" + strftime("%Y-%m-%d<br>%H:%M:%S", localtime()) + "\","
		print_str += "\"chart4_d1\":" + str(random.randint(0,100)) + ","
		print_str += "\"chart4_d2\":" + str(random.randint(0,100)) + "}"

		time.sleep(1)
		print (print_str)
		try:	
			d = json.loads(print_str)
			r = requests.post("http://127.0.0.1:8000/pub", json=d , stream=True , timeout=9999)
#			print(r)
		except KeyboardInterrupt:
			print("stoping...")
			sys.exit(1)
		except:
			print "Unexpected error   :", sys.exc_info()[0]
			sys.exc_clear()
			raise



if __name__ == "__main__":
    main()
