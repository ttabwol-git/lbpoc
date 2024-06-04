"""
main.py: This is the main entry point of the application. It sets up the environment paths,
imports the API configuration, and starts the server

Author: xabi.moreno.maya@gmail.com
Last Updated: 2024-06-04
"""

__version__ = '0.0.1'

import os
import sys
import uvicorn

os.environ['ROOT_PATH'] = os.path.dirname(os.path.abspath(__file__))
os.environ['CONFIG_PATH'] = os.path.join(os.environ['ROOT_PATH'], 'config')
os.environ['API_PATH'] = os.path.join(os.environ['ROOT_PATH'], 'api')
os.environ['ENGINE_PATH'] = os.path.join(os.environ['API_PATH'], 'engine')
os.environ['MANAGERS_PATH'] = os.path.join(os.environ['API_PATH'], 'managers')
os.environ['SERVICES_PATH'] = os.path.join(os.environ['API_PATH'], 'routers')
sys.path.insert(0, os.environ['CONFIG_PATH'])
sys.path.insert(1, os.environ['ENGINE_PATH'])
sys.path.insert(2, os.environ['MANAGERS_PATH'])
sys.path.insert(3, os.environ['SERVICES_PATH'])

from config import APIConfig

app = APIConfig().app

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
