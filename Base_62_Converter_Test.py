from Base_62_Converter import encode62 as encode
from Base_62_Converter import decode62 as decode
from math import floor

# Simple test for Base_62_Converter.py

i = 0
arr = []

while i < 1000:
        arr.append(encode(i))
        print(arr[floor(i/3)], end = '  ')
        i += 3

print('\n\n')
i = 0
while i < 334:
        print(decode(arr[i]), end = '  ')
        i += 1