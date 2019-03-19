#!/usr/bin/env python3

import json

with open('config.json') as json_data_file:
    data = json.load(json_data_file)

with open('config.json.bak', 'w') as outfile:
    json.dump(data, outfile)
