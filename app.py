from flask import Flask, render_template, Response
import pickle
from client import *


app = Flask(__name__)


@app.route("/")
def index():

    return render_template("index.html")


# @app.route('/model_page')
def model():
    return Response(client())


if __name__ == '__main__':
    app.run("88.1.56.23",  port=5011)
