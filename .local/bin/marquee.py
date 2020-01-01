#! /usr/bin/python3
from time import sleep
import sys
import os
music = os.popen('music').read()
string = "{} ... ".format(music)

i = 0
while True:
    print(string[i:] + string[:i])
    sys.stdout.flush()
    i += 1
    if i == len(string):
        i = 0
    sleep(0.15)
