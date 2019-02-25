import json
from flask import Flask
from os import environ
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)


@app.route("/")
def hello():
    redis.incr('counter')
    counter = redis.get('counter').decode("utf-8")
    return json.dumps({
        'msg': 'Hello World!',
        'var': environ.get('YOUR_VAR'),
        'counter': counter
    })


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
