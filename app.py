from flask import Flask, render_template
import client

app = Flask(__name__)

client = client()


@app.route("/")
def index():

    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
