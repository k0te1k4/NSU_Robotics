from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'ex03_tf2_turtles_delay'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your_email@example.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'static_turtle_tf2_broadcaster = ex02_tf2_turtles.static_turtle_tf2_broadcaster:main',
        'turtle_tf2_broadcaster = ex02_tf2_turtles.turtle_tf2_broadcaster:main',
        'turtle_tf2_listener = ex02_tf2_turtles.turtle_tf2_listener:main',
        'fixed_frame_tf2_broadcaster = ex02_tf2_turtles.fixed_frame_tf2_broadcaster:main',
        'dynamic_frame_tf2_broadcaster = ex02_tf2_turtles.dynamic_frame_tf2_broadcaster:main',
        ],
    },
)
