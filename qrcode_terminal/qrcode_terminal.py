#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@author: ‘wang_pc‘
@site: 
@software: PyCharm
@file: qrcode_terminal.py
@time: 2017/2/10 16:38
@Update: 2018/2/6 21:58
'''
import qrcode
from optparse import OptionParser
import sys
import platform

parser = OptionParser()
parser.add_option('-d', '--data', dest='data', help='data to be paser to QRCode')
parser.add_option('-s', '--size', type='choice', choices = ['s','m','l','S','M','L'], dest='size',default='s', help='QRCode size,you can choose S/M/L')

BLOCK = ['█', '▀', '▄', ' ']

def qr_terminal_str(str,version=1):
    qr = qrcode.QRCode(version)
    qr.add_data(str)
    qr.make()
    qr_map = []
    qr_width, qr_height = len(qr.modules), len(qr.modules[0])
    qr_width += 2
    qr_height += 2
    qr_map = [[0 for _ in range(qr_width)] for _ in range(qr_height)]
    for row_id, row in enumerate(qr.modules):
        for col_id, pixel in enumerate(row):
            qr_map[row_id+1][col_id+1] = 1 if pixel else 0
    output = ""
    for row in range(0, len(qr_map), 2):
        for col in range(0, len(qr_map[0])):
            pixel_cur = qr_map[row][col] 
            pixel_below = 1
            if row < len(qr_map) - 1:
                pixel_below = qr_map[row+1][col]
            pixel_encode = pixel_cur << 1 | pixel_below
            output += BLOCK[pixel_encode]
        output += '\n'
    return output[:-1]

def draw(str,version=1):
    output = qr_terminal_str(str,version)
    print (output)


def draw_cmd():
    (options, args) = parser.parse_args()
    if not options.data:
        options.data = sys.stdin.readline()[:-1]
    if not options.data:
        print ('data must be specified. see %s -h' % sys.argv[0])
    else:
        size = options.size
        if size == 'm' or size == 'M':
            version = 3
        elif size == 'l' or size == 'L':
            version = 5
        else:
            version = 1
        draw(options.data,version)

if __name__ == '__main__':
    draw_cmd()
