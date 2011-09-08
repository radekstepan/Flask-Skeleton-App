#!/usr/bin/python
# -*- coding: utf -*-

import random, os

# config settings to save
cfg = {
    'FLASK_PORT' : 5000,
    'DEBUG' : True,
    'SECRET_KEY' : '',
    'MONGODB_HOST' : 'localhost',
    'MONGODB_PORT' : 27017,
    'MONGODB_DB' : ''
}

# flask app port
while True:
    input_port = raw_input('Flask app port (default 5000) ')

    if not input_port:
        cfg['FLASK_PORT'] = 5000
        break

    if input_port:
        cfg['FLASK_PORT'] =  int(input_port.strip()) # Better to use Regex to contraint this
        break

cfg['SECRET_KEY'] = ''.join([random.choice('./ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789') for i in range(30)])

# write config.py
python_code = []
for key, value in cfg.items():
    if isinstance(value, str):
        value = "'" + value.replace("'", r"\'") + "'"
    python_code.append("%s = %s" % (key, value))

with open(os.getcwd() + '/config.py', 'w') as f:
    f.write('\n'.join(python_code))

# write cherrypy.conf
conf =\
'''[global]
server.socket_host = '0.0.0.0'
server.socket_port = %i
server.environment = "production"
tree.mount = {'/' : create_flask_app.application}
''' % cfg['FLASK_PORT']

with open(os.getcwd() + '/cherrypy.conf', 'w') as f:
    f.write(conf)

print('\nConfiguration files written successfully.\n')
