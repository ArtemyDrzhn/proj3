import logging

import requests
from flask import Flask


app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)


@app.route("/")
def index():
    rs = requests.get("https://vk.com/")
    repos = rs.json()
    return repos['updated_at']


if __name__ == '__main__':
    app.run(port=5000)