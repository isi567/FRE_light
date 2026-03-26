import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import socket # Use network instead of serial

class SafetyBridge(Node):
    def __init__(self):
        super().__init__('safety_light_bridge')
        
        # This is the "Magic Address" that points from Docker back to your Mac
        self.host = 'host.docker.internal'
        self.port = 2000 
        
        self.get_logger().info("Safety Bridge started. Waiting for ROS 2 messages...")

        # Subscribe to 'robot_status' topic
        self.subscription = self.create_subscription(
            Int32,
            'robot_status',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        try:
            # Create a temporary network connection to the Mac
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(2) # Don't hang forever if Mac is asleep
                s.connect((self.host, self.port))
                
                if msg.data == 1:
                    s.sendall(b'G')
                    self.get_logger().info("Sent: Green")
                elif msg.data == 2:
                    s.sendall(b'Y')
                    self.get_logger().info("Sent: Yellow")
                elif msg.data == 3:
                    s.sendall(b'R')
                    self.get_logger().info("Sent: Red")
                    
        except Exception as e:
            self.get_logger().error(f"Could not reach Mac Relay: {e}")

def main(args=None):
    rclpy.init(args=args)
    node = SafetyBridge()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()