#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2 == 0:
        subtract_value = 0
    else:
        subtract_value = 32
    print('{}'.format(chr(i - subtract_value)), end='')
