import Jetson.GPIO as GPIO
import time

# 1. Setup
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)

# Define our pins
RED = 15 
YELLOW = 13
GREEN = 11
ALL_PINS = [RED, YELLOW, GREEN]

print(f"Forcing Pins {ALL_PINS} to ON...")

try:
    # 2. Initialize all pins as outputs
    GPIO.setup(ALL_PINS, GPIO.OUT)
    
    # 3. Turn them all HIGH
    GPIO.output(ALL_PINS, GPIO.HIGH)
    
    print("All lights should be glowing! Press Ctrl+C to stop.")
    
    # Keep the script running so the pins stay powered
    while True:
        time.sleep(1)
        
except Exception as e:
    print(f"Error: {e}")
finally:
    # Cleanup turns the pins back off when you exit
    GPIO.cleanup()