import Jetson.GPIO as GPIO
import time

# Use TEGRA_SOC mode
GPIO.setmode(GPIO.TEGRA_SOC)

# Use the Raw Kernel IDs for Orin Nano
GREEN = 444
YELLOW = 422
RED = 428

print(f"Testing Raw IDs: Green({GREEN}), Yellow({YELLOW}), Red({RED})")

try:
    GPIO.setup([GREEN, YELLOW, RED], GPIO.OUT, initial=GPIO.LOW)
    
    while True:
        print("RED ON (ID 428)")
        GPIO.output(RED, GPIO.HIGH)
        time.sleep(1)
        
        print("RED OFF")
        GPIO.output(RED, GPIO.LOW)
        time.sleep(1)
        
except Exception as e:
    print(f"Error: {e}")
finally:
    GPIO.cleanup()