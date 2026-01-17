#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class KeyListener(Node):
    def __init__(self):
        super().__init__('key_listener')
        self.subscription = self.create_subscription(
            String,
            'keyboard_chatter',
            self.listener_callback,
            10
        )
        self.get_logger().info("Keyboard Listener Ready!")

    def listener_callback(self, msg):
        self.get_logger().info(f'Received: "{msg.data}"')

def main():
    rclpy.init()
    node = KeyListener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

