from setuptools import setup
import os
from glob import glob
from setuptools import setup

package_name = 'draw_shape'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name,'launch'),
glob(os.path.join('launch','*launch.[pxy][yma]*')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yahboom',
    maintainer_email='jmarcotte227@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'shape_sub = draw_shape.shape_sub:main',
            'go_to_point = draw_shape.go_to_point_server:main'
        ],
    },
)
