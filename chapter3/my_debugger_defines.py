#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: MapzChen
# Email: 61966578@qq.com

# windows only

from ctypes import *

# 重命名数据类型来解禁win32风格

WORD = c_ushort
DWORD = c_ulong
LPBYTE = POINTER(c_ubyte)
LPTSTR = POINTER(c_char)
HANDLE = c_void_p

# 常量
DEBUG_PROCESS = 0x00000001
CREATE_NEW_CONSOLE = 0x00000010
