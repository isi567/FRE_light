import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import Jetson.GPIO as GPIO

# Define physical pin numbers (Board Mode)
LED_GREEN = 11
LED_YELLOW = 13
LED_RED = 15

class SafetyLightBridge(Node):
    def __init__(self):
        super().__init__('safety_light_bridge')
        
        # Initialize GPIO
        GPIO.setmode(GPIO.BOARD)
        self.pins = [LED_GREEN, LED_YELLOW, LED_RED]
        GPIO.setup(self.pins, GPIO.OUT, initial=GPIO.LOW)
        
        self.get_logger().info("Jetson GPIO Safety Bridge Active (Pins 11, 13, 15)")

        self.subscription = self.create_subscription(
            Int32,
            'robot_status',
            self.listener_callback,
            10)

    def turn_off_all(self):
        GPIO.output(self.pins, GPIO.LOW)

    def listener_callback(self, msg):
        self.turn_off_all() # Reset all lights before setting the new one
        
        if msg.data == 1: # OK
            GPIO.output(LED_GREEN, GPIO.HIGH)
            self.get_logger().info("Status: OK (Green)")
        elif msg.data == 2: # WARNING
            GPIO.output(LED_YELLOW, GPIO.HIGH)
            self.get_logger().info("Status: WARNING (Yellow)")
        elif msg.data == 3: # EMERGENCY
            GPIO.output(LED_RED, GPIO.HIGH)
            self.get_logger().info("Status: EMERGENCY (Red)")
        else:
            self.get_logger().warn(f"Unknown Status Received: {msg.data}")

    def __del__(self):
        GPIO.cleanup()

def main(args=None):
    rclpy.init(args=args)
    node = SafetyLightBridge()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()