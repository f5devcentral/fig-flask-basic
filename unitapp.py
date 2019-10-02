import sys
import importlib 

sys.path.insert(0, './venv/lib/python3.6/site-packages')
ws = importlib.import_module('basic_ws', 'basic_ws.py')

def application(environ, start_response):
    ''' This dispatches requests to our application through WSGI '''
    return ws.app.wsgi_app(environ, start_response)