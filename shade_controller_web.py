# Web-facing portion of Pi Shade Controller App

import os
from flask import Flask, render_template, request


app = Flask('pi-shade-controller')
app.config['DEBUG'] = False

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == "POST":
        if 'Raise' in request.form:
            print("Up")
            pass
        elif 'Lower' in request.form:
            print("Down")
            pass
    return render_template('index.html')






if __name__=='__main__':
    app.run(host='0.0.0.0') # development flag