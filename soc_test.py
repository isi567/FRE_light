import Jetson.GPIO as GPIO
import time

# Use the physical pin numbers (1-40)
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)

# These are the PHYSICAL holes on the board
RED = 15 
YELLOW = 13
GREEN = 11

print("Forcing Pin 15 (Red) to Output...")

try:
    # This is where the 'invalid' error usually happens
    GPIO.setup(RED, GPIO.OUT)
    
    while True:
        print("RED ON")
        GPIO.output(RED, GPIO.HIGH)
        time.sleep(1)
        print("RED OFF")
        GPIO.output(RED, GPIO.LOW)
        time.sleep(1)
        
except Exception as e:
    print(f"Error: {e}")
finally:
    GPIO.cleanup()