from flask import Flask, render_template, Response
import pickle
# from client import *


app = Flask(__name__)


@app.route("/")
def index():

    return render_template("index.html")


@app.route('/model_page')
def model():
    return Response(load_model())


if __name__ == '__main__':
    app.run(debug=True)
