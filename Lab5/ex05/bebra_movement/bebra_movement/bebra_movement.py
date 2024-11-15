import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class SnakeMovement(Node):
    def __init__(self):
        super().__init__('snake_movement')

        self.publisher = self.create_publisher(Twist, '/robot/cmd_vel', 10)
        self.timer_period = 0.1  # seconds
        self.timer = self.create_timer(self.timer_period, self.movement)

        self.direction = 1  # Направление поворота: 1 - вправо, -1 - влево
        self.turn_duration = 1.0  # Длительность поворота в секундах
        self.turn_counter = 0  # Счетчик времени поворота

    def movement(self):
        twister = Twist()

        if self.turn_counter < self.turn_duration / self.timer_period:
            # Поворот
            twister.linear.x = 0.2  # Линейная скорость при повороте
            twister.angular.z = 0.5 * self.direction  # Угловая скорость
            self.turn_counter += 1
        else:
            # Прямолинейное движение
            twister.linear.x = 0.5  # Линейная скорость
            twister.angular.z = 0.0  # Угловая скорость

            # Меняем направление поворота
            if self.turn_counter >= self.turn_duration / self.timer_period:
                self.direction *= -1
                self.turn_counter = 0

        self.publisher.publish(twister)


def main(args=None):
    rclpy.init(args=args)
    node = SnakeMovement()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()