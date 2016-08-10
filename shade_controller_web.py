# Web-facing portion of Pi Shade Controller App

import os
from flask import Flask, render_template


app = Flask('pi-shade-controller')
app.config['DEBUG'] = False

@app.route('/')
def index():
    return render_template('index.html')






if __name__=='__main__':
    app.run(host='0.0.0.0') # development flag