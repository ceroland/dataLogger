#!/usr/bin/python
import time

print("Start : %s" % time.ctime())
for i in range(15):
    print(".", end="", flush=True)
    time.sleep(0.5)
#print("\nEnd : %s" % time.ctime())
#    time.sleep(3)
print(chr(27) + "[2J") # or print('\x1b[2J')
