# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 18:56:37 2020

@author: chris
"""

import os
import json


file_name = 'config.json'


try:
    file = open(file_name, 'r')
    #config = file.read()
    config = json.load(file)
    file.close()
except IOError:
    file = open(file_name, 'w')
    config = {}
    config['modFolder'] = 'sti til modfolder'
    config['baseFolder'] = 'annen sti'
    file.write(json.dumps(config))
    file.close()

print(config)

