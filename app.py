import flask
from redis import Redis
import os


app = flask.Flask(__name__, static_url_path="", static_folder = "static")
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    hits = int(redis.get('hits'))
    return flask.render_template('index.html', visits=hits)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
