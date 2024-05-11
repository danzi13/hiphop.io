from flask import Flask, render_template, Response, request, jsonify
import datetime
from datetime import datetime

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
