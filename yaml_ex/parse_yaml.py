#!/usr/bin/env python2

import yaml

with open('config.yaml', 'r') as ymlfile:
  cfg = yaml.load(ymlfile)

for section in cfg:
  print(section)

print(cfg['mysql'])
print(cfg['other'])
