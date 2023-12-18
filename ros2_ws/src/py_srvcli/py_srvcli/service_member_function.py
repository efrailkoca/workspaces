from tutorial_interfaces.srv import AddThreeInts					# change

import rclpy
from rclpy.node import Node


class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.srv = self.create_service(AddThreeInts, 'add_three_ints', self.add_three_ints_callback)								# change

    def add_three_ints_callback(self, request, response):				# change
        response.sum = request.a + request.b + request.c				# change
        self.get_logger().info('Incoming request\na: %d b: %d c: %d' % (request.a, request.b, request.c))										# change

        return response


def main():
    rclpy.init()

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
