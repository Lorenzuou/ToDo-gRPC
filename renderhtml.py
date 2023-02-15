#webserver to server client.html

# Path: toDo/client.html
import flask
from flask import request, jsonify
import requests
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
todos = [
    {'id': 0,
        'description': 'Buy milk'},
    {'id': 1,
        'description': 'Buy bread'},
    {'id': 2,
        'description': 'Buy eggs'}

]

@app.route('/', methods=['GET'])
def home():
    #render index.html
    return flask.render_template('index.html')

#run the server
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
