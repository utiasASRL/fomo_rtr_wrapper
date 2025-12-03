from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'fomo_rtr_wrapper'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
	(os.path.join('share', package_name, 'launch'),
        glob(os.path.join('launch', '*launch.[pxy][yma]*'))), # This line adds the launch files
        (os.path.join('share', package_name, 'config'),
        glob(os.path.join('config', '*.[pxy][yma]*')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='alec',
    maintainer_email='freakyfactoid@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        "start_rtr_fomo = fomo_rtr_wrapper.start_repeat:main"
        ],
    },
)
