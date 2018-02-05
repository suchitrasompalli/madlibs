"""Main application code handling http requests."""
from flask import Flask, render_template


app = Flask(__name__)


APPLICATION_NAME = "MadLibs"


@app.route('/')
@app.route('/madlibs/')
def showMainPage():
    """Main page."""
    return render_template('generate.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
