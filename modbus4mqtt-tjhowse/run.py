#!/usr/bin/env python3
import json
import subprocess

if __name__ == '__main__':
    with open('/data/options.json') as file:
        options = json.load(file)
    command = ['modbus4mqtt'] + [f'--{key} {options[key]}' for key in options]
    subprocess.run(command)
