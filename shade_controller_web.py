# Web-facing portion of Pi Shade Controller App

import os
from flask import Flask, render_template, request
import shade_controller_hw as hw


MANUAL_CONTROLS = {'Raise':"up",'Lower':"down"}
RESPONSES = {'up':"Raising",'down':"Lowering"}
HW_RESPONSE = {'up':hw.up,'down':hw.down}

app = Flask('pi-shade-controller')
app.config['DEBUG'] = False

@app.route('/')
def index():
    return render_template('index.html', buttons=MANUAL_CONTROLS)

@app.route('/<button>')
def control(button=None):
    response = RESPONSES[button] + " shade"
    print(response)
    HW_RESPONSE[button]()
    return response, 200, {'Content-Type': 'text/plain'}


if __name__=='__main__':
    app.run(host='0.0.0.0') # development flag