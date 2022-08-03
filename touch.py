import time
from grove.gpio import GPIO

touch1 = GPIO(10, GPIO.IN)
touch2 = GPIO(10, GPIO.IN)
touch3 = GPIO(10, GPIO.IN)
touch4 = GPIO(10, GPIO.IN)
touch5 = GPIO(10, GPIO.IN)
touch1_last = 0
touch2_last = 0
touch3_last = 0
touch4_last = 0
touch5_last = 0

while True:
	touch1_current = touch1.read()
	touch2_current = touch2.read()
	touch3_current = touch3.read()
	touch4_current = touch4.read()
	touch5_current = touch5.read()
	
	if touch1_current == 1 and touch1_last == 0:        
	    print("Sensor 1 tocado")
	elif touch1_current == 0 and touch1_last == 1:
	    print("Sensor 1 solto")        
	touch1_last = touch1_current

	if touch2_current == 1 and touch2_last == 0:        
	    print("Sensor 2 tocado")
	elif touch2_current == 0 and touch2_last == 1:
	    print("Sensor 2 solto")        
	touch2_last = touch2_current

	if touch3_current == 1 and touch3_last == 0:        
	    print("Sensor 3 tocado")
	elif touch3_current == 0 and touch3_last == 1:
	    print("Sensor 3 solto")        
	touch3_last = touch3_current

	if touch4_current == 1 and touch4_last == 0:        
	    print("Sensor 4 tocado")
	elif touch4_current == 0 and touch4_last == 1:
	    print("Sensor 4 solto")        
	touch4_last = touch4_current

	if touch5_current == 1 and touch5_last == 0:        
	    print("Sensor 5 tocado")
	elif touch5_current == 0 and touch5_last == 1:
	    print("Sensor 5 solto")        
	touch5_last = touch5_current

	time.sleep(0.1)