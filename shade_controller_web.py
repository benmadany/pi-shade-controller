# Web-facing portion of Pi Shade Controller App

import os
from flask import Flask, render_template, request
import shade_controller_hw as hw


app = Flask('pi-shade-controller')
app.config['DEBUG'] = False

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == "POST":
        if 'Raise' in request.form:
            print("Up")
            hw.up()
            pass
        elif 'Lower' in request.form:
            print("Down")
            hw.down()
            pass
    return render_template('index.html')






if __name__=='__main__':
    app.run(host='0.0.0.0') # development flag