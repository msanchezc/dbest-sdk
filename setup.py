#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

import sys

if sys.version_info < (3, 8):
    sys.exit("Sorry, Python < 3.8 is not supported")

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open("requirements.txt", "r") as fh:
    requirements = fh.readlines()

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="IoTDeco",
    author_email='contacto@iotdeco.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.8',
    ],
    description="A Python package for remote control of DBEST (drone battery exchanger system for DJI Mavic 2 products)",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords=["dbest", "sdk", "dji", "mavic",
              "battery", "exchanger", "robotic"],
    name='dbest_sdk',
    packages=find_packages(include=['dbest_sdk', 'dbest_sdk.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/PSBPOSAS/dbest-sdk',
    version='0.1.1',
    zip_safe=False,
)
