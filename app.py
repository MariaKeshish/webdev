from flask import render template, Flask, request 
import json

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    #with open('index.html', 'r') as f:
     #content = f.read()
    #return content
    return render_template('index.html')

@app.route('/map.html')
def map():
    #with open('map.html', 'r') as f:
     #content = f.read()
    #return content
    return render_template('map.html')

@app.route('/women.html')
def women():
    #with open('women.html', 'r') as f:
     #content = f.read()
    #return content
    return render_template('women.html')