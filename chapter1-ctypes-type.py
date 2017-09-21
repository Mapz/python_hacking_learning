#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: MapzChen
# Email: 61966578@qq.com

from ctypes import *
# int
a = c_int(10)
print(a)

# u short
b = c_ushort(-5)
print(b)

#char pointer
char_pointer = c_char_p(b"this is c chars")
print(char_pointer)
print(char_pointer.value)

#struct
class waterBottle(Structure):
    _fields_ = [
        ("water",c_float),
        ("bottle_cap",c_float)
    ]

a_bottle_of_water = waterBottle(10,102)
print(a_bottle_of_water)
print(a_bottle_of_water.water)
print(a_bottle_of_water.bottle_cap)

#union
class amount(Union):
    _fields_ = [
        ("long",c_long),
        ("int",c_int),
        ("char",c_char * 8)
    ]
input_value = input("Enter value of amount:")
amount_value = amount(int(input_value))
print(amount_value.long)
print(amount_value.int)
print(amount_value.char)