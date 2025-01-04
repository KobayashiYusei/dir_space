import os
import shutil
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class diskSpace(Node):
    def __init__(self):
        super().__init__('disk_space')
        self.pub = self.create_publisher(Float64, 'disk_space', 10)
        self.timer = self.create_timer(1.0, self.cb)

    def cb(self):
        try:
            total, used, free = shutil.disk_usage('/')
            free_gb = free / (2**30)
            usage = used/total * 100
            msg = Float64()
            msg.data = float(free_gb)
            self.pub.publish(msg)
            self.get_logger().info(f"Free disk space: {free_gb:.2f} GB Usage:{usage:.2f}%")
        except Exception as e:
            self.get_logger().error(f"Failed to calculate disk space: {e}")

def main(args=None):
    rclpy.init(args=args)
    node = diskSpace()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
