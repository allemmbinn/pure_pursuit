import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist


class Vehicle():

    def __init__(self, lin_v= 0.5, lookahead_dist = 0.6):
        self.lin_v = lin_v
        self.lookahead_dist = lookahead_dist

class PurePursuit(Node):

    def __init__(self):
        super().__init__('pure_pursuit_controller')
        self.subscription = self.create_subscription(
            Odometry,
            'odom',
            self.execute,
            10)
        self.subscription  # prevent unused variable warning
        #To publish the values to the topic /cmd_vel
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
    
    def execute(self, msg):
        pass

    def timer_callback(self):
        msg = Twist()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1
        



def main(args=None):
    rclpy.init(args=args)

    purepursuit = PurePursuit()

    rclpy.spin(purepursuit)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    purepursuit.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()