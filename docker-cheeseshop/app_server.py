import os
import time
import requests

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/liveness')
def liveness():
    return render_template('liveness.html')

@app.route('/readiness')
def readiness():
    return render_template('readiness.html')

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/shutdown", methods=['GET'])
def stop():
    shutdown_func = request.environ.get('werkzeug.server.shutdown')
    if shutdown_func is None:
        raise RuntimeError('Not running werkzeug')
    
    shutdown_func()

    return "Stopping Server...."

def start(port):
    print("Starting Server....")
    app.run(host='0.0.0.0', port=port, use_debugger=True, use_reloader=False)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5050))
    start(port)