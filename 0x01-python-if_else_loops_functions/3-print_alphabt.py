#!/usr/bin/python3
for j in range(ord('a'), ord('z') + 1):
    if chr(j) != 'e' and chr(j) != 'q':
        print("{:c}".format(j), end='')
