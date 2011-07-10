from cherrypy import wsgiserver
from app import app

wsgi_apps = [('/', app)]
server = wsgiserver.CherryPyWSGIServer(('0.0.0.0', 5006), wsgi_apps, request_queue_size=500, server_name='localhost')

if __name__ == '__main__':
    try:
        server.start()
    except KeyboardInterrupt:
        server.stop()
