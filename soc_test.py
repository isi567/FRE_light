import Jetson.GPIO as GPIO
import time

# Use the physical pin numbers (1-40)
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)

# These are the PHYSICAL holes on the board
RED = 15 
YELLOW = 11
GREEN = 13

print("Forcing Pin 13 (Green) to Output...")

try:
    # This is where the 'invalid' error usually happens
    GPIO.setup(GREEN, GPIO.OUT)
    
    while True:
        print("GREEN ON")
        GPIO.output(GREEN, GPIO.HIGH)
        time.sleep(1)
        print("GREEN OFF")
        GPIO.output(GREEN, GPIO.LOW)
        time.sleep(1)
        
except Exception as e:
    print(f"Error: {e}")
finally:
    GPIO.cleanup()