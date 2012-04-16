A skeleton Flask, CherryPy, MongoDB app.

## Requirements

- Flask, <code>easy_install flask</code>
- CherryPy WSGI Server, <code>easy_install cherrypy</code> (for production)

## Installation

- Run the install script <code>python install.py</code> and choose the port the app will run at (default is 5000)
- Configure MongoDB database settings in <code>config.py</code> (optional)

## Running
### Flask/Werkzeug Server (for development)

The app can be run through the Werkzeug WSGI server that comes with Flask. To run it, execute <code>python flask_app.py</code>.
Provided you have set <code>DEBUG = True</code> in your <code>config.py</code> file, this option will give you an interactive debugger and your app will be reloaded if changes to source files are detected.

### CherryPy WSGI Server (for production)

1. Run <code>./start_server.sh</code>. This will launch <code>cherryd</code> with settings coming from <code>cherrypy.conf</code> that uses an 'in-between' script <code>create_flask_app.py</code> to attach the Flask Object to the server
2. A file, <code>cherrypy.pid</code> will be created that has the id of the process running
3. Calling <code>./stop_server.sh</code> will read the .pid file and kill the process waiting for child threads to terminate
