import os
import shutil
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class DiskSpacePublisher(Node):
    def __init__(self):
        super().__init__('disk_space_publisher')
        self.publisher_ = self.create_publisher(Float64, 'disk_space', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)  # Publish every second
        self.directory = '/'
        self.get_logger().info(f"Publishing disk space for directory: {self.directory}")

    def timer_callback(self):
        try:
            total, used, free = shutil.disk_usage(self.directory)
            free_gb = free / (1024**3)  # Convert bytes to gigabytes
            msg = Float64()
            msg.data = float(free_gb)  # Ensure the value is a float
            self.publisher_.publish(msg)
            self.get_logger().info(f"Free disk space: {free_gb:.2f} GB")
        except Exception as e:
            self.get_logger().error(f"Failed to calculate disk space: {e}")

def main(args=None):
    rclpy.init(args=args)
    node = DiskSpacePublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
