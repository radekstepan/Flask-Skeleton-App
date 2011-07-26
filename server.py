import config
from cherrypy import wsgiserver
from app import app

wsgi_apps = [('/', app)]
server = wsgiserver.CherryPyWSGIServer(('0.0.0.0', config.FLASK_PORT), wsgi_apps, request_queue_size=500, server_name='localhost')

if __name__ == '__main__':
    try:
        server.start()
    except KeyboardInterrupt:
        server.stop()
