from flask import Flask, url_for, render_template
from markupsafe import escape

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/configuration', methods=['GET'])
def configuration():
    return 'Configuration Main'

@app.route('/configuration/commit_time/<int:seconds>', methods=['GET'])
def set_commit_time(seconds):
    return "Setting the commit time to {} seconds".format(seconds)