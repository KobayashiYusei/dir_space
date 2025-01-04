import os
import shutil
import sys
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class diskSpace(Node):
    def __init__(self, path):
        super().__init__('disk_space')
        self.pub = self.create_publisher(Float64, 'disk_space', 10)
        self.timer = self.create_timer(1.0, self.cb)
        self.path = path
        if not os.path.exists(self.path):
            self.get_logger().error(f"path does not exist: {self.path}")
            self.path = '/' 
            sys.exit(1)
        self.get_logger().info(f"Publish disk space of{self.path}")

    def cb(self):
        try:
            total, used, free = shutil.disk_usage(self.path)
            free_gb = free / (2**30)
            msg = Float64()
            msg.data = float(free_gb)
            self.pub.publish(msg)
        except Exception as e:
            self.get_logger().error(f"Failed to calculate disk space: {e}")

def main(args=None):
    rclpy.init(args=args)
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = '/'
    node = diskSpace(path)
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
