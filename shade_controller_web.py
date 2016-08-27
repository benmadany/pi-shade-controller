# Web-facing portion of Pi Shade Controller App

import signal, sys
from flask import Flask, render_template, request
import shade_controller_monitor as scm


MANUAL_CONTROLS = {'Raise':"up",'Lower':"down"}
RESPONSES = {'up':"Raising",'down':"Lowering"}

monitor = scm.Monitor()
hwresponse = {'up':monitor.manualup,'down':monitor.manualdown}

app = Flask('pi-shade-controller')
app.config['DEBUG'] = False

@app.route('/')
def index():
    return render_template('index.html', buttons=MANUAL_CONTROLS)

@app.route('/<button>')
def control(button=None):
    response = RESPONSES[button] + " shade"
    print(response)
    hwresponse[button]()
    return response, 200, {'Content-Type': 'text/plain'}

def shutdown(signal, frame):
    monitor.cleanup()
    sys.exit(0)

if __name__=='__main__':
    signal.signal(signal.SIGINT, shutdown)
    monitor.autochange()
    app.run(host='0.0.0.0') # development flag
