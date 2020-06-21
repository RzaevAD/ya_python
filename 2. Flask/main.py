from flask import Flask, request
from flask.json import jsonify

app = Flask(__name__)


@app.route('/client/info')
def client_info():
    return jsonify({'user_agent': str(request.user_agent)})


if __name__ == '__main__':
    app.run('127.0.0.1', '8000')
