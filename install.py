#!/usr/bin/python
# -*- coding: utf -*-

import random, os

# config settings to save
cfg = {
    'MONGODB_HOST' : 'localhost',
    'MONGODB_PORT' : 27017,
    'MONGODB_DB' : '',
    'DEBUG' : True,
    'SECRET_KEY' : ''
}

# mongodb host
while True:
    cfg['MONGODB_HOST'] = raw_input('MongoDB host (usually localhost): ').strip()
    if cfg['MONGODB_HOST']:
        break

# mongodb port
while True:
    cfg['MONGODB_PORT'] = int(raw_input('MongoDB port (usually 27017) ').strip())
    if cfg['MONGODB_PORT']:
        break

# mongodb database name
while True:
    cfg['MONGODB_DB'] = raw_input('MongoDB database: ').strip()
    if cfg['MONGODB_DB']:
        break

cfg['SECRET_KEY'] = ''.join([random.choice('./ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789') for i in range(30)])

python_code = []
for key, value in cfg.items():
    if isinstance(value, str):
        value = "'" + value.replace("'", r"\'") + "'"
    elif isinstance(value, list):
        value = '[]'
    python_code.append("%s = %s" % (key, value))

with open(os.getcwd() + '/config.py', 'w') as f:
    f.write('\n'.join(python_code))

print('\nConfiguration file written successfully.\n')