from flask import render_template, Flask, request 
import json

app=Flask(__name__)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="127.0.0.1", port=5000)
    app.run(debug=True)

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/map.html')
def map():
    return render_template('map.html')

@app.route('/women.html')
def women():
    return render_template('women.html')