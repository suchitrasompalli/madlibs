"""Main application code handling http requests."""
from __future__ import print_function
from flask import Flask, render_template, request

import sys

app = Flask(__name__)

APPLICATION_NAME = "MadLibs"


@app.route('/')
@app.route('/madlibs/', methods=['GET', 'POST'])
def showMainPage():
    """Main page."""
    if request.method == 'POST':
        print(request.form["madlib-text"], file=sys.stderr)
        file = open("madlib.txt", "w")
        file.write(request.form["madlib-text"])
        file.close()
        return render_template('success.html')
    else:
        return render_template('generate.html')


@app.route('/madlibs/play/')
def showPlayPage():
    """Play page."""
    file = open("madlib.txt", "r")
    madlibData = ''
    for line in file:
        madlibData += line
    return render_template('play.html', madlibData=madlibData)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
