import Jetson.GPIO as GPIO
try:
    GPIO.setmode(GPIO.BOARD)
    print("✅ Success! The Jetson model was recognized.")
    print(f"Board Model: {GPIO.model}")
except Exception as e:
    print(f"❌ Still failing: {e}")
finally:
    GPIO.cleanup()