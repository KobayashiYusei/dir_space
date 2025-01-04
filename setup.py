from setuptools import find_packages, setup

package_name = 'dir_space'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Kobayashi Yusei',
    maintainer_email='s23C1054AF@s.chibakoudai.jp',
    description='指定したファイルシステムの空き容量を提示します',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
		'pub_node = dir_space.pub_node:main'
        ],
    },
)
