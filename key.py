#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class KeyPublisher(Node):
    def __init__(self):
        super().__init__('key_publisher')
        self.publisher_ = self.create_publisher(String, 'keyboard_chatter', 10)
        self.get_logger().info("Keyboard Publisher Ready! Type something and press Enter:")

    def publish_message(self, msg_text):
        msg = String()
        msg.data = msg_text
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published: "{msg.data}"')

def main():
    rclpy.init()
    node = KeyPublisher()
    try:
        while True:
            msg_text = input("Enter message: ")
            if msg_text.lower() in ['exit', 'quit']:
                break
            node.publish_message(msg_text)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
