#!/usr/bin/env python3

import subprocess
import time

APP_NAME = '\'/sbin/init\''

cmd_arg1 = 'ps -ef'.split()
cmd_arg2 = ('grep %s' % APP_NAME).split()
cmd_arg3 = 'wc -l'.split()

print(' | '.join([' '.join(cmd_arg1), ' '.join(cmd_arg2), ' '.join(cmd_arg3)]) )

def exec_command():

    p1 = subprocess.Popen(cmd_arg1, stdin=subprocess.PIPE, stdout=subprocess.PIPE) 
    p2 = subprocess.Popen(cmd_arg2, stdin=p1.stdout, stdout=subprocess.PIPE)
    p3 = subprocess.Popen(cmd_arg3, stdin=p2.stdout, stdout=subprocess.PIPE)

    process_count = int(p3.communicate()[0].strip())
    return process_count

flag = False

while True:

    process_count = exec_command()

    print('[+] Monitoring ...')
    print('[-] # of processed : %d' % process_count)
    if process_count >= 1 and not flag:
        print('Process {} exists and init'.format(APP_NAME))
        flag = True
    elif process_count < 1 and flag:
        print('Process {} does not exist and destroy'.format(APP_NAME))
        flag = False

    time.sleep(1)
