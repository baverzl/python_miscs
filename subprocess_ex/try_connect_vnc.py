#!/usr/bin/env python

import os
import time
import subprocess
from threading import Timer

cmd = 'nc 192.168.43.3 5901'
cmd = cmd.split()

while True:
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    def timer_func():
        print('[-] Connect Failed: device not ready...')
        proc.kill()

    timer = Timer(2, timer_func)
    try:
        timer.start()
        res = proc.communicate()[0][:3]
    except Exception:
        continue
    finally:
        timer.cancel()

    if len(res) == 0:
        print('[-] Connect Failed: Empty string received...')
        time.sleep(2)
        continue

    if res.decode() == 'RFB':
        print('[*] Connected successfully')
        os.system('xtightvncviewer 192.168.43.3:1')
        break
