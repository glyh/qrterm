#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@author: ‘wang_pc‘
@site: 
@software: PyCharm
@file: setup.py
@time: 2017/2/10 16:18
'''
from setuptools import setup

setup(
    name='qrterm',
    version='0.8',
    license='MIT',
    author_email='840652591@qq.com',
    url='https://github.com/alishtory/qrterm',
    description='Python QRCode Terminal',
    platforms=['any'],
    py_modules= ['qrterm'],
    packages= ['qrterm'],
    entry_points={
        'console_scripts': [
            'qrterm-py= qrterm.qrterm:draw_cmd',
        ],
    },
    install_requires=['Pillow', 'qrcode'],
    include_package_data=True,
)
