#!/usr/bin/python3
for l in range(ord('a'), ord('z') + 1):
    if chr(l) != 'e' and chr(l) != 'q':
        print("{:c}".format(l), end='')
