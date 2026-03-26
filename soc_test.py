import Jetson.GPIO as GPIO
import time

# Use TEGRA_SOC mode for Orin Nano
GPIO.setmode(GPIO.TEGRA_SOC)

# These are the direct hardware addresses for Pins 11, 13, and 15
GREEN = "PAC.06"
YELLOW = "PR.04"
RED = "PD.01"

print(f"Testing SOC Pins: {GREEN}, {YELLOW}, {RED}")

try:
    GPIO.setup([GREEN, YELLOW, RED], GPIO.OUT, initial=GPIO.LOW)
    
    while True:
        print("RED ON")
        GPIO.output(RED, GPIO.HIGH)
        time.sleep(1)
        
        print("RED OFF")
        GPIO.output(RED, GPIO.LOW)
        time.sleep(1)
        
except KeyboardInterrupt:
    print("Stopping...")
finally:
    GPIO.cleanup()