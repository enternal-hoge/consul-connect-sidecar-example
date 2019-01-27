# coding: utf-8

from flask import Flask
app = Flask(__name__)

@app.route('/page')
def hello_world():
    return '{ message: "page" }'

@app.route('/ja')
def hello_world_ja():
    return '{ message: "ぱげ"}'

@app.route('/ping')
def ping():
    return '{ result: "ok"}'

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
