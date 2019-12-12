#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

setup(
    name='waddle_geoportal',
    version='1.0',
    description='waddle, a c2cgeoportal project',
    author='waddle',
    author_email='info@waddle.com',
    url='https://www.waddle.com/',
    install_requires=[
        'c2cgeoportal_geoportal',
        'c2cgeoportal_admin',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'paste.app_factory': [
            'main = waddle_geoportal:main',
        ],
        'console_scripts': [
        ],
    },
)
