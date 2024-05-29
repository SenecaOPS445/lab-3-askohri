#!/usr/bin/env python3
# Author Name: askohri
# Author ID: 142112226

import subprocess

def free_space():
    command_output = subprocess.getoutput('df -h | grep \'/$\' | awk \'{print $4}\'')
    return command_output.strip()

if __name__ == '__main__':
    print(free_space())
