import sys
import zklib
import time
import zklib.zkconst

zk = zklib.zkdevice
zk = zklib.device("192.168.1.2", 4370)
ret = zk.connect()
print("connection:")
