#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: MapzChen
# Email: 61966578@qq.com

from ctypes import *
from platform import *

cdll_names = {
    'Darwin':'libc.dylib',
    'Windows':'msvcrt.dll',
    'Linux':'libc.so.6',
}

clib = cdll.LoadLibrary(cdll_names[system()])
message_string = b"hello world\n"
clib.printf(b"Testing:%s", message_string)
