import os
from setuptools import find_packages, setup

from icecast_influxdb_stats import __version__


with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='icecast-influxdb-stats',
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'influxdb',
        'requests'
    ],
    license='GPL-3.0',
    description='Sends Icecast status to InfluxDB',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/fm-futura/icecast-influxdb-stats',
    author='Adrián Pardini',
    author_email='github@tangopardo.com.ar',
    entry_points={
        'console_scripts': [
            'icecast-listeners-to-influxdb=icecast_influxdb_stats.icecast_influxdb_stats:main'
        ]
    },
    classifiers=[
        'Environment :: Web Environment',
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Telecommunications Industry',
        'License :: OSI Approved :: GNU General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Communications',
    ],
    keywords='radio, icecast, streaming, influx',
)
